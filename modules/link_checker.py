
import re
from urllib.parse import urlparse

SHORTENED_DOMAINS = {
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "is.gd",
    "cutt.ly",
    "shorturl.at"
}

def check_url(url):
    url = url.strip()

    if not url:
        return {
            "valid": False,
            "findings": ["Please enter a URL."]
        }

    if not re.match(r"^https?://", url, re.IGNORECASE):
        url = "https://" + url

    try:
        parsed = urlparse(url)
        hostname = parsed.hostname

        if not hostname or "." not in hostname:
            raise ValueError("Invalid hostname")

    except ValueError:
        return {
            "valid": False,
            "findings": ["The URL format appears invalid."]
        }

    findings = []

    if parsed.scheme != "https":
        findings.append("The link does not use HTTPS.")

    if hostname.lower() in SHORTENED_DOMAINS:
        findings.append("This is a URL-shortening service.")

    if "@" in parsed.netloc:
        findings.append("The URL contains an unusual @ symbol.")

    if hostname.lower().startswith("xn--"):
        findings.append("The domain uses an internationalised encoding.")

    if re.search(r"\d+\.\d+\.\d+\.\d+", hostname):
        findings.append("The hostname appears to use an IP address.")

    suspicious_words = [
        "verify-account",
        "login-secure",
        "claim-prize",
        "free-gift",
        "account-suspended"
    ]

    for word in suspicious_words:
        if word in url.lower():
            findings.append(
                "The URL contains a potentially suspicious phrase."
            )
            break

    return {
        "valid": True,
        "hostname": hostname,
        "findings": findings
    }
