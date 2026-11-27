
import json
from datetime import datetime, timedelta, timezone

import streamlit as st
import streamlit.components.v1 as components

from modules.ui_theme import apply_theme


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Global Intelligence | ScamShield AI",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_theme()


# =========================================================
# DESIGN SYSTEM — NAVY + ELECTRIC BLUE
# =========================================================

st.markdown("""
<style>
.block-container {
    max-width: 100% !important;
    padding: 1.2rem 2rem 2.5rem !important;
}

.stApp {
    background:
        radial-gradient(ellipse at 85% 0%, rgba(39,100,210,0.10), transparent 38%),
        linear-gradient(145deg, #071225 0%, #09172C 55%, #07101F 100%);
}

.globe-eyebrow {
    color: #82B4FF;
    font-size: .7rem;
    font-weight: 850;
    letter-spacing: 2.8px;
    margin-bottom: 13px;
}

.globe-title {
    font-size: clamp(2.5rem, 4.8vw, 4rem);
    line-height: 1.08;
    font-weight: 900;
    letter-spacing: -2.4px;
    color: #F1F6FF;
    margin-bottom: 15px;
}

.globe-title span {
    background: linear-gradient(100deg, #58A5FF, #83D8FF);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.globe-description {
    color: #A5B7D4;
    font-size: .96rem;
    line-height: 1.85;
    max-width: 800px;
    margin-bottom: 20px;
}

.module-label {
    color: #83B7FF;
    font-size: .69rem;
    font-weight: 850;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 15px 0 13px;
}

div[data-baseweb="select"] > div {
    background: #101F38;
    border: 1px solid rgba(119,165,235,.27);
    border-radius: 12px;
    min-height: 48px;
}

div[data-baseweb="select"] span {
    color: #E5EEFF;
}

div[data-baseweb="select"]:hover > div {
    border-color: #579BFA;
}

div.stButton > button {
    border-radius: 11px;
    min-height: 45px;
    font-weight: 800;
    border: 1px solid rgba(112,165,255,.35);
    background: linear-gradient(110deg, #2467CF, #258CCB);
    color: #FFFFFF;
    transition: all .22s ease;
}

div.stButton > button:hover {
    border-color: #A7CEFF;
    background: linear-gradient(110deg, #347BE8, #269EDB);
    color: #FFFFFF;
    transform: translateY(-2px);
    box-shadow: 0 9px 24px rgba(38,112,215,.2);
}

[data-testid="stPageLink"] a {
    border-radius: 11px;
    font-weight: 800;
    border: 1px solid rgba(112,165,255,.28);
    background: rgba(22,52,91,.65);
    color: #C9DEFF;
    transition: all .2s ease;
}

[data-testid="stPageLink"] a:hover {
    border-color: #579BFA;
    background: rgba(37,103,207,.25);
    color: #FFFFFF;
}

[data-testid="stCaptionContainer"] {
    color: #849BBC;
}

hr {
    border-color: rgba(120,160,220,.17) !important;
}

div[data-testid="stAlert"] {
    background: rgba(22,48,83,.55);
    border: 1px solid rgba(104,157,239,.25);
    border-radius: 14px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: linear-gradient(145deg, rgba(18,35,63,.9), rgba(10,22,42,.96));
    border: 1px solid rgba(117,153,220,.18);
    border-radius: 17px;
}

h1, h2, h3 {
    color: #EDF4FF !important;
    letter-spacing: -.5px;
}

p {
    color: #A9B9D3;
    line-height: 1.8;
}

@media(max-width: 768px) {
    .block-container {
        padding: 1rem 1rem 2rem !important;
    }

    .globe-title {
        letter-spacing: -1.5px;
    }
}
</style>
""", unsafe_allow_html=True)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="globe-eyebrow">SCAMSHIELD AI / GLOBAL INTELLIGENCE</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="globe-title">Explore the <span>connected world.</span></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="globe-description">'
    'Explore Earth through interactive 3D geography, '
    'NASA satellite imagery and a public internet routing feed.'
    '</div>',
    unsafe_allow_html=True
)

left, right = st.columns([4, 1])

with left:
    st.caption("GLOBAL VIEW / EARTH OBSERVATION / LIVE BGP")

with right:
    st.page_link("app.py", label="← Command Centre")


# =========================================================
# LOCATIONS
# =========================================================

LOCATIONS = {
    "Global view": (10, 20, 3.2),
    "India": (78.9629, 20.5937, 2.6),
    "New Delhi, India": (77.2090, 28.6139, 2.0),
    "Mumbai, India": (72.8777, 19.0760, 2.0),
    "London, United Kingdom": (-0.1276, 51.5072, 2.0),
    "New York, United States": (-74.0060, 40.7128, 2.0),
    "Singapore": (103.8198, 1.3521, 1.9),
    "Tokyo, Japan": (139.6917, 35.6895, 2.0),
    "Dubai, United Arab Emirates": (55.2708, 25.2048, 2.0),
    "São Paulo, Brazil": (-46.6333, -23.5505, 2.0),
    "Johannesburg, South Africa": (28.0473, -26.2041, 2.0),
}

if "globe_destination" not in st.session_state:
    st.session_state["globe_destination"] = "Global view"

control_left, control_right = st.columns([3, 1])

with control_left:
    selected_location = st.selectbox(
        "Explore a location",
        list(LOCATIONS.keys()),
        index=list(LOCATIONS.keys()).index(
            st.session_state["globe_destination"]
        )
    )

with control_right:
    st.write("")
    if st.button("Explore location ↗", use_container_width=True):
        st.session_state["globe_destination"] = selected_location
        st.rerun()

destination = st.session_state["globe_destination"]
lon, lat, distance = LOCATIONS[destination]

initial_view = json.dumps({
    "lon": lon,
    "lat": lat,
    "distance": distance
})

nasa_date = (
    datetime.now(timezone.utc) - timedelta(days=2)
).strftime("%Y-%m-%d")


# =========================================================
# THREE.JS GLOBE
# =========================================================

globe_html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
* { box-sizing: border-box; }

html, body {
    margin: 0;
    width: 100%;
    height: 100%;
    overflow: hidden;
    background: #050A16;
    font-family: Arial, sans-serif;
}

#scene {
    width: 100%;
    height: 100%;
    min-height: 680px;
    position: relative;
    overflow: hidden;
    background:
        radial-gradient(ellipse at center, #142B50 0%, #09172E 48%, #030711 100%);
    border: 1px solid rgba(100,160,255,.20);
    border-radius: 18px;
}

canvas {
    display: block;
    width: 100%;
    height: 100%;
}

@media(min-width:1100px) {
    #scene {
        height: 82vh;
        min-height: 750px;
    }
}

@media(max-width:1099px) {
    #scene { min-height: 580px; }
    #fullscreen { display: none; }
}

html.frame-fullscreen,
body.frame-fullscreen {
    width: 100% !important;
    height: 100% !important;
    overflow: hidden !important;
}

.frame-fullscreen #scene {
    width: 100vw !important;
    height: 100vh !important;
    min-height: 100vh !important;
    border-radius: 0;
}

#fullscreen {
    position: absolute;
    top: 17px;
    right: 17px;
    z-index: 20;
    border: 1px solid rgba(120,165,255,.4);
    background: rgba(8,13,28,.94);
    color: #E9EDFF;
    border-radius: 9px;
    padding: 11px 15px;
    cursor: pointer;
    font-size: 12px;
    font-weight: 700;
}

#fullscreen:hover, #reset:hover {
    background: rgba(35,92,170,.95);
    border-color: #83B7FF;
}

#status {
    position: absolute;
    top: 17px;
    left: 17px;
    z-index: 5;
    color: #E9EDFF;
    background: rgba(8,13,28,.92);
    border: 1px solid rgba(120,165,255,.25);
    padding: 11px 15px;
    border-radius: 9px;
    font-size: 11px;
    letter-spacing: 1px;
    pointer-events: none;
}

#status span { color: #65B9FF; }

#live-panel {
    position: absolute;
    top: 65px;
    left: 17px;
    z-index: 8;
    width: 265px;
    max-height: 300px;
    overflow: hidden;
    color: #E9EDFF;
    background: rgba(8,16,34,.94);
    border: 1px solid rgba(100,160,255,.32);
    border-radius: 12px;
    padding: 14px;
    pointer-events: none;
    backdrop-filter: blur(12px);
    box-shadow: 0 12px 35px rgba(0,0,0,.24);
}

#live-heading {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 10px;
    letter-spacing: 1.4px;
    color: #AEB9D8;
    margin-bottom: 9px;
}

#live-state {
    color: #F0B65D;
    font-size: 9px;
}

#live-count {
    font-size: 30px;
    font-weight: 800;
    color: #81B9FF;
    line-height: 1.2;
}

#live-subtitle {
    color: #8999BC;
    font-size: 10px;
    margin-top: 3px;
}

#live-events {
    border-top: 1px solid rgba(120,165,255,.18);
    margin-top: 10px;
    padding-top: 7px;
    max-height: 130px;
    overflow: hidden;
}

.live-event {
    font-size: 10px;
    color: #BFCBE7;
    padding: 5px 0;
    border-bottom: 1px solid rgba(120,165,255,.08);
    line-height: 1.5;
    overflow-wrap: anywhere;
}

.live-event strong {
    color: #91B8FF;
    font-weight: 600;
}

#legend {
    position: absolute;
    left: 17px;
    bottom: 28px;
    z-index: 5;
    padding: 13px 16px;
    color: #DCE5FF;
    background: rgba(8,13,28,.92);
    border: 1px solid rgba(120,165,255,.25);
    border-radius: 10px;
    font-size: 11px;
    line-height: 1.9;
    pointer-events: none;
}

.dot {
    display: inline-block;
    height: 7px;
    width: 7px;
    background: #65B9FF;
    border-radius: 50%;
    margin-right: 8px;
}

.line {
    display: inline-block;
    height: 2px;
    width: 17px;
    background: #55AFFF;
    margin-right: 8px;
    vertical-align: middle;
}

#loading {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    color: #E9EDFF;
    gap: 12px;
    pointer-events: none;
    z-index: 3;
}

#loading.hidden { display: none; }

#loader {
    width: 32px;
    height: 32px;
    border: 3px solid rgba(120,165,255,.2);
    border-top-color: #65B9FF;
    border-radius: 50%;
    animation: spin .8s linear infinite;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}

#message {
    color: #AEB9D8;
    font-size: 12px;
    text-align: center;
    padding: 0 15px;
}

#reset {
    position: absolute;
    right: 18px;
    bottom: 25px;
    z-index: 6;
    border: 1px solid rgba(120,165,255,.3);
    background: rgba(8,13,28,.94);
    color: #E9EDFF;
    border-radius: 9px;
    padding: 10px 14px;
    cursor: pointer;
    font-weight: 700;
}

#error {
    display: none;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%,-50%);
    color: #E9EDFF;
    text-align: center;
    width: 85%;
    z-index: 10;
    font-size: 13px;
}

@media(max-width:600px) {
    #live-panel {
        width: 205px;
        top: 62px;
        max-height: 240px;
    }
    #live-events { max-height: 85px; }
    #legend { font-size: 9px; }
}
</style>
</head>

<body>

<div id="scene">

    <div id="status">
        <span>●</span> SCAMSHIELD / NASA EARTH
    </div>

    <button id="fullscreen" type="button">
        ⛶ Expand Globe
    </button>

    <div id="live-panel">
        <div id="live-heading">
            <span>LIVE INTERNET ROUTING</span>
            <span id="live-state">CONNECTING</span>
        </div>

        <div id="live-count">0</div>
        <div id="live-subtitle">
            BGP announcements received · Session total
        </div>

        <div id="live-events">
            <div class="live-event">
                Waiting for the first routing update...
            </div>
        </div>
    </div>

    <div id="loading">
        <div id="loader"></div>
        <strong>CONNECTING TO EARTH OBSERVATION</strong>
        <div id="message">Loading NASA satellite imagery...</div>
    </div>

    <div id="legend">
        <div><span class="dot"></span>Global country network dots</div>
        <div><span class="line"></span>Illustrative connections</div>
        <div style="color:#91A4D0;">
            Public BGP events · Not physical device locations
        </div>
    </div>

    <button id="reset">Reset view ↗</button>
    <div id="error"></div>

</div>

<script type="importmap">
{
    "imports": {
        "three": "https://cdn.jsdelivr.net/npm/three@0.170.0/build/three.module.js",
        "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.170.0/examples/jsm/",
        "topojson-client": "https://cdn.jsdelivr.net/npm/topojson-client@3/+esm"
    }
}
</script>

<script type="module">

import * as THREE from "three";
import { OrbitControls } from
"three/addons/controls/OrbitControls.js";
import * as topojson from "topojson-client";

const initialView = __INITIAL_VIEW__;
const nasaDate = "__NASA_DATE__";

const container = document.getElementById("scene");
const loading = document.getElementById("loading");
const message = document.getElementById("message");
const errorBox = document.getElementById("error");
const fullscreenButton = document.getElementById("fullscreen");

let renderer;
let camera;
let controls;


/* ==================================================
   FULLSCREEN
================================================== */

const frame = window.frameElement;

function resizeGlobe() {
    if (!renderer || !camera) return;

    const width = container.clientWidth;
    const height = container.clientHeight;

    if (!width || !height) return;

    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
}

function updateFullscreenState() {
    try {
        const isFullscreen =
            window.parent.document.fullscreenElement === frame;

        document.documentElement.classList.toggle(
            "frame-fullscreen", isFullscreen
        );

        document.body.classList.toggle(
            "frame-fullscreen", isFullscreen
        );

        fullscreenButton.textContent = isFullscreen
            ? "✕ Exit Globe"
            : "⛶ Expand Globe";

        setTimeout(resizeGlobe, 150);

    } catch (error) {
        console.warn(error);
    }
}

fullscreenButton.addEventListener("click", async () => {
    try {
        const parentDocument = window.parent.document;

        if (parentDocument.fullscreenElement) {
            await parentDocument.exitFullscreen();
        } else if (frame && frame.requestFullscreen) {
            await frame.requestFullscreen();
        } else {
            await container.requestFullscreen();
        }

    } catch (error) {
        console.error("Fullscreen unavailable:", error);
    }
});

try {
    window.parent.document.addEventListener(
        "fullscreenchange", updateFullscreenState
    );
} catch (error) {
    console.warn(error);
}

document.addEventListener(
    "fullscreenchange", updateFullscreenState
);


/* ==================================================
   SCENE
================================================== */

try {

    const scene = new THREE.Scene();
    scene.background = new THREE.Color("#050A16");

    camera = new THREE.PerspectiveCamera(
        38,
        container.clientWidth / container.clientHeight,
        0.1,
        1000
    );

    camera.position.set(0, 0, initialView.distance);

    renderer = new THREE.WebGLRenderer({
        antialias: true,
        alpha: false,
        powerPreference: "high-performance"
    });

    renderer.setPixelRatio(
        Math.min(window.devicePixelRatio || 1, 1.75)
    );

    renderer.setSize(
        container.clientWidth,
        container.clientHeight
    );

    renderer.outputColorSpace = THREE.SRGBColorSpace;
    renderer.toneMapping = THREE.ACESFilmicToneMapping;
    renderer.toneMappingExposure = 1.15;

    container.appendChild(renderer.domElement);


    /* ORBIT CONTROLS */

    controls = new OrbitControls(
        camera,
        renderer.domElement
    );

    controls.enableDamping = true;
    controls.dampingFactor = 0.045;
    controls.enablePan = false;
    controls.minDistance = 1.35;
    controls.maxDistance = 5.5;
    controls.autoRotate = true;
    controls.autoRotateSpeed = 0.45;


    /* LIGHTING */

    scene.add(new THREE.AmbientLight(0xffffff, 1.15));

    const sunlight = new THREE.DirectionalLight(
        0xffffff, 2.2
    );

    sunlight.position.set(5, 3, 5);
    scene.add(sunlight);


    /* STARS */

    const starGeometry = new THREE.BufferGeometry();
    const starPositions = [];

    for (let i = 0; i < 1800; i++) {
        starPositions.push(
            (Math.random() - 0.5) * 35,
            (Math.random() - 0.5) * 35,
            (Math.random() - 0.5) * 35
        );
    }

    starGeometry.setAttribute(
        "position",
        new THREE.Float32BufferAttribute(starPositions, 3)
    );

    const stars = new THREE.Points(
        starGeometry,
        new THREE.PointsMaterial({
            color: 0xB8CCFF,
            size: 0.035,
            transparent: true,
            opacity: 0.8
        })
    );

    scene.add(stars);


    /* EARTH */

    const earthGroup = new THREE.Group();
    scene.add(earthGroup);

    const earth = new THREE.Mesh(
        new THREE.SphereGeometry(1, 128, 128),
        new THREE.MeshPhongMaterial({
            color: 0x2876B8,
            shininess: 18,
            specular: new THREE.Color(0x345B91)
        })
    );

    earthGroup.add(earth);


    /* ATMOSPHERE */

    const atmosphere = new THREE.Mesh(
        new THREE.SphereGeometry(1.035, 96, 96),
        new THREE.ShaderMaterial({

            vertexShader: `
                varying vec3 vNormal;
                void main() {
                    vNormal = normalize(normalMatrix * normal);
                    gl_Position = projectionMatrix *
                        modelViewMatrix * vec4(position, 1.0);
                }
            `,

            fragmentShader: `
                varying vec3 vNormal;
                void main() {
                    float intensity = pow(
                        0.72 - dot(vNormal, vec3(0.0,0.0,1.0)),
                        3.0
                    );
                    gl_FragColor = vec4(
                        0.22, 0.48, 1.0, intensity * 0.65
                    );
                }
            `,

            blending: THREE.AdditiveBlending,
            side: THREE.BackSide,
            transparent: true,
            depthWrite: false
        })
    );

    earthGroup.add(atmosphere);


    /* ==================================================
       NASA GIBS SATELLITE IMAGERY
    ================================================== */

    const textureLoader = new THREE.TextureLoader();
    textureLoader.setCrossOrigin("anonymous");

    const nasaLayer =
        "VIIRS_SNPP_CorrectedReflectance_TrueColor";

    function nasaWmsUrl(date) {
        const params = new URLSearchParams({
            SERVICE: "WMS",
            REQUEST: "GetMap",
            VERSION: "1.1.1",
            LAYERS: nasaLayer,
            STYLES: "",
            FORMAT: "image/jpeg",
            SRS: "EPSG:4326",
            BBOX: "-180,-90,180,90",
            WIDTH: "4096",
            HEIGHT: "2048",
            TIME: date
        });

        return (
            "https://gibs.earthdata.nasa.gov/wms/epsg4326/best/wms.cgi?"
            + params.toString()
        );
    }

    function loadEarthFallback() {

        message.textContent = "Loading Earth texture...";

        textureLoader.load(
            "https://threejs.org/examples/textures/planets/earth_atmos_2048.jpg",

            texture => {
                texture.colorSpace = THREE.SRGBColorSpace;

                earth.material.dispose();

                earth.material = new THREE.MeshPhongMaterial({
                    map: texture,
                    color: 0xffffff,
                    shininess: 18,
                    specular: new THREE.Color(0x345B91)
                });

                message.textContent = "Earth texture loaded.";
                loading.classList.add("hidden");
            },

            undefined,

            error => {
                console.warn("Earth texture fallback failed:", error);

                earth.material.dispose();

                earth.material = new THREE.MeshPhongMaterial({
                    color: 0x2876B8,
                    shininess: 25,
                    specular: new THREE.Color(0x567DB5)
                });

                message.textContent =
                    "Satellite texture unavailable. Showing blue Earth.";

                loading.classList.add("hidden");
            }
        );
    }


    function loadNASAImage(date, attemptsLeft = 3) {

        message.textContent =
            "Requesting NASA VIIRS imagery for " + date;

        textureLoader.load(
            nasaWmsUrl(date),

            texture => {

                texture.colorSpace = THREE.SRGBColorSpace;

                texture.anisotropy =
                    renderer.capabilities.getMaxAnisotropy();

                earth.material.dispose();

                earth.material = new THREE.MeshPhongMaterial({
                    map: texture,
                    color: 0xffffff,
                    shininess: 18,
                    specular: new THREE.Color(0x345B91)
                });

                message.textContent =
                    "NASA VIIRS imagery loaded · " + date;

                document.getElementById("status").innerHTML =
                    "<span>●</span> NASA VIIRS / " + date;

                loading.classList.add("hidden");
            },

            undefined,

            error => {

                console.warn("NASA imagery failed:", error);

                if (attemptsLeft > 1) {

                    const previousDate = new Date(
                        date + "T00:00:00Z"
                    );

                    previousDate.setUTCDate(
                        previousDate.getUTCDate() - 1
                    );

                    const fallbackDate =
                        previousDate.toISOString().slice(0, 10);

                    loadNASAImage(fallbackDate, attemptsLeft - 1);

                } else {

                    loadEarthFallback();

                }
            }
        );
    }

    loadNASAImage(nasaDate);


    /* ==================================================
       GEOGRAPHIC COORDINATES
    ================================================== */

    function coordinatesToVector(
        lon, lat, radius = 1.012
    ) {
        const longitude = THREE.MathUtils.degToRad(lon);
        const latitude = THREE.MathUtils.degToRad(lat);

        return new THREE.Vector3(
            -radius * Math.cos(latitude) * Math.sin(longitude),
            radius * Math.sin(latitude),
            radius * Math.cos(latitude) * Math.cos(longitude)
        );
    }


    /* ==================================================
       GLOBAL COUNTRY DOT NETWORK
    ================================================== */

    const countryDotMaterial = new THREE.PointsMaterial({
        color: 0x65B9FF,
        size: 0.009,
        sizeAttenuation: true,
        transparent: true,
        opacity: 0.88,
        depthWrite: false,
        blending: THREE.AdditiveBlending
    });

    let countryDots = null;
    let totalCountryDots = 0;
    let countryCount = 0;

    function pointInsideRing(point, ring) {

        const x = point[0];
        const y = point[1];

        let inside = false;

        for (
            let i = 0, j = ring.length - 1;
            i < ring.length;
            j = i++
        ) {
            const xi = ring[i][0];
            const yi = ring[i][1];
            const xj = ring[j][0];
            const yj = ring[j][1];

            const intersects =
                ((yi > y) !== (yj > y)) &&
                (
                    x <
                    (xj - xi) * (y - yi) /
                    ((yj - yi) || 0.0000001) + xi
                );

            if (intersects) inside = !inside;
        }

        return inside;
    }


    function pointInsidePolygon(lon, lat, polygon) {

        if (!polygon || !polygon.length) return false;

        if (!pointInsideRing([lon, lat], polygon[0])) {
            return false;
        }

        for (let i = 1; i < polygon.length; i++) {
            if (pointInsideRing([lon, lat], polygon[i])) {
                return false;
            }
        }

        return true;
    }


    function getPolygonBounds(ring) {

        let minLon = 180;
        let maxLon = -180;
        let minLat = 90;
        let maxLat = -90;

        ring.forEach(point => {
            minLon = Math.min(minLon, point[0]);
            maxLon = Math.max(maxLon, point[0]);
            minLat = Math.min(minLat, point[1]);
            maxLat = Math.max(maxLat, point[1]);
        });

        return {minLon, maxLon, minLat, maxLat};
    }


    function createCountryDots(features) {

        const positions = [];

        let processedCountries = 0;

        features.forEach(feature => {

            if (!feature.geometry) return;

            const geometry = feature.geometry;

            let polygons = [];

            if (geometry.type === "Polygon") {
                polygons = [geometry.coordinates];
            } else if (geometry.type === "MultiPolygon") {
                polygons = geometry.coordinates;
            } else {
                return;
            }

            const usablePolygons = polygons.filter(
                polygon =>
                    polygon &&
                    polygon[0] &&
                    polygon[0].length >= 4
            );

            if (!usablePolygons.length) return;

            processedCountries++;

            const targetDots = 32;

            let countryAdded = 0;
            let attempts = 0;
            const maximumAttempts = targetDots * 100;

            while (
                countryAdded < targetDots &&
                attempts < maximumAttempts
            ) {

                attempts++;

                const polygon =
                    usablePolygons[
                        Math.floor(
                            Math.random() * usablePolygons.length
                        )
                    ];

                const bounds = getPolygonBounds(polygon[0]);

                if (
                    !Number.isFinite(bounds.minLon) ||
                    !Number.isFinite(bounds.maxLon) ||
                    bounds.maxLon - bounds.minLon < 0.0001 ||
                    bounds.maxLat - bounds.minLat < 0.0001
                ) {
                    continue;
                }

                const randomLon =
                    bounds.minLon +
                    Math.random() * (bounds.maxLon - bounds.minLon);

                const randomLat =
                    bounds.minLat +
                    Math.random() * (bounds.maxLat - bounds.minLat);

                if (
                    !pointInsidePolygon(
                        randomLon,
                        randomLat,
                        polygon
                    )
                ) {
                    continue;
                }

                const position = coordinatesToVector(
                    randomLon,
                    randomLat,
                    1.012
                );

                positions.push(
                    position.x,
                    position.y,
                    position.z
                );

                countryAdded++;
            }
        });

        const geometry = new THREE.BufferGeometry();

        geometry.setAttribute(
            "position",
            new THREE.Float32BufferAttribute(positions, 3)
        );

        const points = new THREE.Points(
            geometry,
            countryDotMaterial
        );

        points.frustumCulled = false;

        earthGroup.add(points);

        countryDots = points;
        totalCountryDots = positions.length / 3;
        countryCount = processedCountries;

        document.getElementById("status").innerHTML =
            "<span>●</span> GLOBAL NETWORK / " +
            totalCountryDots.toLocaleString() + " DOTS";

        console.log(
            "Country network loaded:",
            countryCount,
            "countries;",
            totalCountryDots,
            "dots"
        );
    }


    async function loadCountryBoundaries() {

        try {

            message.textContent =
                "Building global country network...";

            const response = await fetch(
                "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json"
            );

            if (!response.ok) {
                throw new Error("Country boundary data unavailable");
            }

            const worldData = await response.json();

            const countries = topojson.feature(
                worldData,
                worldData.objects.countries
            );

            createCountryDots(countries.features);

        } catch (error) {

            console.warn(
                "Country network could not load:",
                error
            );

            document.getElementById("status").innerHTML =
                "<span>●</span> NASA EARTH / NETWORK DOTS UNAVAILABLE";
        }
    }

    loadCountryBoundaries();


    /* ==================================================
       GEOGRAPHIC NODES
    ================================================== */

    const nodes = [
        {name:"London", lon:-0.1276, lat:51.5072},
        {name:"New York", lon:-74.0060, lat:40.7128},
        {name:"Mumbai", lon:72.8777, lat:19.0760},
        {name:"Singapore", lon:103.8198, lat:1.3521},
        {name:"Tokyo", lon:139.6917, lat:35.6895},
        {name:"São Paulo", lon:-46.6333, lat:-23.5505},
        {name:"Johannesburg", lon:28.0473, lat:-26.2041}
    ];

    const nodeGeometry =
        new THREE.SphereGeometry(0.012, 16, 16);

    const nodeMaterial = new THREE.MeshBasicMaterial({
        color: 0x78B8FF
    });

    const nodeMeshes = [];

    nodes.forEach(node => {

        const point = new THREE.Mesh(
            nodeGeometry,
            nodeMaterial.clone()
        );

        point.position.copy(
            coordinatesToVector(node.lon, node.lat)
        );

        earthGroup.add(point);
        nodeMeshes.push(point);
    });


    /* ==================================================
       ILLUSTRATIVE CONNECTIONS
    ================================================== */

    const connections = [
        ["London", "New York"],
        ["London", "Mumbai"],
        ["Mumbai", "Singapore"],
        ["Singapore", "Tokyo"],
        ["Singapore", "Johannesburg"],
        ["New York", "São Paulo"],
        ["Mumbai", "Tokyo"]
    ];

    const connectionLines = [];

    connections.forEach(pair => {

        const start = nodes.find(n => n.name === pair[0]);
        const end = nodes.find(n => n.name === pair[1]);

        if (!start || !end) return;

        const startVector = coordinatesToVector(
            start.lon, start.lat, 1.008
        );

        const endVector = coordinatesToVector(
            end.lon, end.lat, 1.008
        );

        const middle = startVector.clone()
            .add(endVector)
            .multiplyScalar(0.5)
            .normalize()
            .multiplyScalar(1.2);

        const curve = new THREE.QuadraticBezierCurve3(
            startVector,
            middle,
            endVector
        );

        const lineMaterial = new THREE.LineBasicMaterial({
            color: 0x55AFFF,
            transparent: true,
            opacity: 0.72
        });

        const line = new THREE.Line(
            new THREE.BufferGeometry().setFromPoints(
                curve.getPoints(80)
            ),
            lineMaterial
        );

        earthGroup.add(line);
        connectionLines.push(line);
    });


    /* ==================================================
       REAL LIVE BGP DATA — RIPE RIS LIVE
    ================================================== */

    const liveCountElement =
        document.getElementById("live-count");

    const liveStateElement =
        document.getElementById("live-state");

    const liveEventsElement =
        document.getElementById("live-events");

    let bgpCount = 0;
    let eventPulse = 0;
    let reconnectDelay = 2000;
    let bgpSocket = null;
    let reconnectTimer = null;

    function setLiveState(text, color) {
        liveStateElement.textContent = text;
        liveStateElement.style.color = color;
    }

    function addLiveEvent(data) {

        const event = document.createElement("div");
        event.className = "live-event";

        const asn = data.peer_asn || "Unknown";
        const collector = data.host || "RIPE RIS";

        let prefix = "Prefix information unavailable";

        if (
            Array.isArray(data.announcements) &&
            data.announcements.length > 0
        ) {
            const firstAnnouncement = data.announcements[0];

            if (
                firstAnnouncement.prefixes &&
                firstAnnouncement.prefixes.length > 0
            ) {
                prefix = firstAnnouncement.prefixes[0];
            }
        }

        const eventTime = data.timestamp
            ? new Date(data.timestamp * 1000).toLocaleTimeString()
            : new Date().toLocaleTimeString();

        event.textContent =
            eventTime + " · AS" + asn +
            " · " + prefix +
            " · " + collector;

        liveEventsElement.prepend(event);

        while (liveEventsElement.children.length > 5) {
            liveEventsElement.removeChild(
                liveEventsElement.lastChild
            );
        }

        eventPulse = 1;

        nodeMeshes.forEach(node => {
            node.scale.setScalar(1.8);
        });

        connectionLines.forEach(line => {
            line.material.opacity = 1;
        });

        console.log("Live BGP event:", {
            peer_asn: asn,
            peer: data.peer || "Unknown",
            collector: collector,
            prefix: prefix,
            time: eventTime
        });
    }

    function connectRIS() {

        if (
            bgpSocket &&
            (
                bgpSocket.readyState === WebSocket.OPEN ||
                bgpSocket.readyState === WebSocket.CONNECTING
            )
        ) {
            return;
        }

        setLiveState("CONNECTING", "#F0B65D");

        const socketURL =
            "wss://ris-live.ripe.net/v1/ws/?client=scamshield-ai";

        try {
            bgpSocket = new WebSocket(socketURL);
        } catch (error) {
            setLiveState("UNAVAILABLE", "#FF7777");
            scheduleReconnect();
            return;
        }

        bgpSocket.onopen = () => {

            reconnectDelay = 2000;

            setLiveState("LIVE", "#65E6A5");

            bgpSocket.send(JSON.stringify({
                type: "ris_subscribe",
                data: {
                    type: "UPDATE",
                    host: "rrc00",
                    require: "announcements",
                    socketOptions: {
                        acknowledge: true
                    }
                }
            }));

            console.log("Connected to RIPE RIS Live");
        };

        bgpSocket.onmessage = event => {

            let message;

            try {
                message = JSON.parse(event.data);
            } catch (error) {
                return;
            }

            if (message.type === "ris_subscribe_ok") {
                setLiveState("LIVE", "#65E6A5");
                return;
            }

            if (message.type === "ris_error") {
                console.warn("RIPE RIS error:", message.data);
                setLiveState("STREAM ERROR", "#FF7777");
                return;
            }

            if (message.type !== "ris_message") return;

            const data = message.data;

            if (!data || data.type !== "UPDATE") return;

            if (
                !Array.isArray(data.announcements) ||
                data.announcements.length === 0
            ) {
                return;
            }

            bgpCount += 1;

            liveCountElement.textContent =
                bgpCount.toLocaleString();

            setLiveState("LIVE", "#65E6A5");

            addLiveEvent(data);
        };

        bgpSocket.onerror = error => {
            console.warn("RIPE RIS connection error:", error);
            setLiveState("RECONNECTING", "#F0B65D");
        };

        bgpSocket.onclose = () => {
            setLiveState("RECONNECTING", "#F0B65D");
            scheduleReconnect();
        };
    }

    function scheduleReconnect() {

        if (reconnectTimer) return;

        reconnectTimer = setTimeout(() => {
            reconnectTimer = null;
            connectRIS();

            reconnectDelay = Math.min(
                reconnectDelay * 1.7,
                30000
            );

        }, reconnectDelay);
    }

    connectRIS();


    /* ==================================================
       CAMERA MOVEMENT
    ================================================== */

    function flyToLocation(lon, lat, distance) {

        const longitude = THREE.MathUtils.degToRad(lon);
        const latitude = THREE.MathUtils.degToRad(lat);

        const target = new THREE.Vector3(
            -Math.cos(latitude) * Math.sin(longitude),
            Math.sin(latitude),
            Math.cos(latitude) * Math.cos(longitude)
        ).multiplyScalar(distance);

        const start = camera.position.clone();
        const started = performance.now();
        const duration = 1500;

        controls.autoRotate = false;

        function animateCamera(now) {

            const progress = Math.min(
                (now - started) / duration,
                1
            );

            const smooth =
                progress * progress * (3 - 2 * progress);

            camera.position.lerpVectors(
                start, target, smooth
            );

            camera.lookAt(0, 0, 0);
            controls.update();

            if (progress < 1) {
                requestAnimationFrame(animateCamera);
            } else {
                controls.autoRotate = true;
            }
        }

        requestAnimationFrame(animateCamera);
    }

    flyToLocation(
        initialView.lon,
        initialView.lat,
        initialView.distance
    );

    document.getElementById("reset").addEventListener(
        "click",
        () => flyToLocation(10, 20, 3.2)
    );

    controls.addEventListener("start", () => {
        controls.autoRotate = false;
    });


    /* ==================================================
       RESIZE
    ================================================== */

    window.addEventListener("resize", resizeGlobe);

    if (window.ResizeObserver) {
        new ResizeObserver(resizeGlobe).observe(container);
    }


    /* ==================================================
       ANIMATION
    ================================================== */

    function animate() {

        requestAnimationFrame(animate);

        controls.update();

        stars.rotation.y += 0.000025;

        eventPulse *= 0.94;

        nodeMeshes.forEach((node, index) => {

            const phase = index * 0.8;

            const idlePulse =
                1 + Math.sin(performance.now() * 0.002 + phase) * 0.12;

            const livePulse =
                1 + eventPulse * 1.5;

            node.scale.setScalar(idlePulse * livePulse);
        });

        connectionLines.forEach(line => {
            line.material.opacity =
                0.55 + eventPulse * 0.4;
        });

        if (countryDotMaterial) {
            countryDotMaterial.opacity =
                0.78 + Math.sin(performance.now() * 0.0015) * 0.10;
        }

        renderer.render(scene, camera);
    }

    animate();

} catch(error) {

    console.error(error);

    loading.classList.add("hidden");
    errorBox.style.display = "block";

    errorBox.textContent =
        "3D Earth could not initialise: " + error.message;
}

</script>
</body>
</html>
"""

globe_html = (
    globe_html
    .replace("__INITIAL_VIEW__", initial_view)
    .replace("__NASA_DATE__", nasa_date)
)


# =========================================================
# DISPLAY GLOBE
# =========================================================

st.markdown(
    '<div class="module-label">● INTERACTIVE 3D GLOBE</div>',
    unsafe_allow_html=True
)

components.html(
    globe_html,
    height=950,
    scrolling=False
)

st.caption(
    f"Current location: {destination} · "
    "Drag to rotate · Scroll to zoom · Reset to return globally"
)

st.caption(
    f"Satellite source: NASA GIBS / VIIRS SNPP · "
    f"Requested observation date: {nasa_date}"
)


# =========================================================
# LIVE NETWORK INTELLIGENCE
# =========================================================

st.write("")
st.divider()

st.markdown(
    '<div class="module-label">LIVE NETWORK INTELLIGENCE</div>',
    unsafe_allow_html=True
)

st.subheader("Real-time BGP routing feed")

st.write(
    "The globe connects to RIPE NCC RIS Live and receives "
    "public BGP UPDATE announcements from the rrc00 route collector."
)

st.info(
    "The live counter and event feed use actual received routing messages. "
    "The country dots show geographic coverage based on country boundaries; "
    "they do not represent actual routers, devices, people or cyberattacks. "
    "The globe pulses are event-triggered visual effects."
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🌍 Geographic Explorer")
    st.write(
        "Navigate the existing 3D Earth and explore "
        "available geographic locations."
    )

with col2:
    st.markdown("### 🛰️ NASA Observation")
    st.write(
        "Satellite imagery from NASA GIBS, subject "
        "to layer availability and observation delay."
    )

with col3:
    st.markdown("### 📡 Cyber Intelligence")
    st.write(
        "Open verified public cyber intelligence reports "
        "through the dedicated intelligence module."
    )

st.page_link(
    "pages/7_Threat_Intelligence.py",
    label="Open Threat Intelligence →"
)


# =========================================================
# PRIVACY
# =========================================================

st.write("")
st.divider()

with st.container(border=True):

    st.markdown("### Privacy and transparency")

    st.write(
        "This explorer uses public routing information and public "
        "geographic boundary data. It does not monitor individuals, "
        "access private camera systems, identify personal devices "
        "or perform personal tracking."
    )

    st.caption(
        "NASA imagery is an Earth observation product. "
        "Country dots represent geographic coverage, not live device "
        "locations. The live BGP feed reports routing messages, while "
        "the globe's geographic connection lines remain illustrative."
    )


# =========================================================
# FOOTER
# =========================================================

st.divider()

st.caption(
    "SCAMSHIELD AI  •  GLOBAL INTELLIGENCE EXPLORER"
)
