
import sqlite3
import re
from pathlib import Path
from datetime import datetime, timezone

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "scamshield_threats.db"

STOP_WORDS = {
    "a", "an", "the", "is", "are", "was", "were",
    "to", "of", "and", "or", "in", "on", "for",
    "me", "my", "i", "he", "she", "they", "we",
    "you", "your", "it", "this", "that", "from",
    "with", "by", "as", "at", "be", "been",
    "someone", "somebody", "person", "recipient"
}

ALIASES = {
    "verification": "otp",
    "code": "otp",
    "passcode": "otp",
    "pretending": "impersonation",
    "claimed": "impersonation",
    "claiming": "impersonation",
    "employee": "bank",
    "representative": "bank",
    "requested": "request",
    "demanded": "request",
    "asked": "request",
    "pressured": "pressure",
    "pressuring": "pressure"
}


def get_connection():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialise_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS threat_reports (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                channel TEXT NOT NULL,
                category TEXT NOT NULL,
                description TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
        """)


def normalise_text(text):
    text = str(text).lower().strip()
    return re.sub(r"\s+", " ", text)


def get_keywords(text):
    words = re.findall(r"[a-z]+", normalise_text(text))
    keywords = set()

    for word in words:
        if word in STOP_WORDS:
            continue

        word = ALIASES.get(word, word)
        keywords.add(word)

    return keywords


def calculate_similarity(text1, text2):
    words1 = get_keywords(text1)
    words2 = get_keywords(text2)

    if not words1 or not words2:
        return 0.0

    common = words1.intersection(words2)
    combined = words1.union(words2)

    return len(common) / len(combined)


def find_similar_reports(
    channel,
    category,
    description,
    threshold=0.25
):
    channel = normalise_text(channel)
    category = normalise_text(category)

    similar_reports = []

    with get_connection() as connection:
        rows = connection.execute("""
            SELECT id, channel, category, description, created_at
            FROM threat_reports
            ORDER BY id DESC
            LIMIT 500
        """).fetchall()

        for report in rows:

            if normalise_text(report["channel"]) != channel:
                continue

            if normalise_text(report["category"]) != category:
                continue

            score = calculate_similarity(
                description,
                report["description"]
            )

            if score >= threshold:
                similar_reports.append({
                    "id": report["id"],
                    "description": report["description"],
                    "similarity": round(score * 100, 1)
                })

    similar_reports.sort(
        key=lambda item: item["similarity"],
        reverse=True
    )

    return similar_reports[:5]


def add_report(channel, category, description):
    channel = str(channel).strip()[:30]
    category = str(category).strip()[:60]
    description = str(description).strip()[:300]

    if not channel or not category or not description:
        raise ValueError("All report fields are required.")

    with get_connection() as connection:

        existing_reports = connection.execute("""
            SELECT channel, category, description
            FROM threat_reports
        """).fetchall()

        for report in existing_reports:
            if (
                normalise_text(report["channel"]) == normalise_text(channel)
                and normalise_text(report["category"]) == normalise_text(category)
                and normalise_text(report["description"]) == normalise_text(description)
            ):
                return None

        created_at = datetime.now(timezone.utc).isoformat()

        cursor = connection.execute("""
            INSERT INTO threat_reports
            (channel, category, description, created_at)
            VALUES (?, ?, ?, ?)
        """, (
            channel,
            category,
            description,
            created_at
        ))

        return cursor.lastrowid


def get_reports(limit=100):
    limit = max(1, min(int(limit), 500))

    with get_connection() as connection:
        rows = connection.execute("""
            SELECT id, channel, category, description, created_at
            FROM threat_reports
            ORDER BY id DESC
            LIMIT ?
        """, (limit,)).fetchall()

        return [dict(row) for row in rows]


def get_report_stats():
    with get_connection() as connection:

        total = connection.execute(
            "SELECT COUNT(*) FROM threat_reports"
        ).fetchone()[0]

        categories = connection.execute("""
            SELECT category, COUNT(*) AS total
            FROM threat_reports
            GROUP BY category
        """).fetchall()

        channels = connection.execute("""
            SELECT channel, COUNT(*) AS total
            FROM threat_reports
            GROUP BY channel
        """).fetchall()

        return {
            "total": total,
            "categories": {
                row["category"]: row["total"]
                for row in categories
            },
            "channels": {
                row["channel"]: row["total"]
                for row in channels
            }
        }


initialise_database()
