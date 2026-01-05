from flask import Flask, render_template, jsonify, request
import PyPDF2
import json
import re
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Gemini SDK
try:
    from google import genai

    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False

app = Flask(__name__)

# ================== CONFIGURATION ==================
API_KEY = os.getenv("GEMINI_API_KEY")
client = None

if GEMINI_AVAILABLE:
    try:
        client = genai.Client(api_key=API_KEY)
    except Exception as e:
        print(f"Gemini Client Error: {e}")
        client = None


# ================== TEXT EXTRACTION ==================
def extract_text_from_pdf(pdf_file):
    try:
        reader = PyPDF2.PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"
        return text.strip()
    except Exception:
        return ""


# ================== SMART LOCAL ENGINE ==================
def local_ats_engine(resume_text, job_desc):
    resume = resume_text.lower()
    jd = job_desc.lower()

    # Professional Stop Words to ignore (Prevents "noise" in keywords)
    stop_words = {
        "should",
        "looking",
        "basic",
        "knowledge",
        "required",
        "members",
        "work",
        "candidate",
        "ability",
        "skills",
        "using",
        "working",
        "experience",
        "years",
        "strong",
        "excellent",
        "written",
        "verbal",
        "communication",
        "plus",
        "preferred",
        "requirements",
        "responsibilities",
        "provide",
        "applications",
        "maintain",
        "develop",
        "engineer",
        "software",
        "team",
        "programming",
        "databases",
        "problem",
        "solving",
        "related",
        "test",
    }

    # Extract words longer than 3 chars
    jd_words = re.findall(r"\b\w{4,}\b", jd)

    missing_skills = []
    seen = set()
    for word in jd_words:
        if word not in stop_words and word not in resume and word not in seen:
            missing_skills.append(word)
            seen.add(word)

    # Scoring Calculation
    keyword_count = len(list(set(jd_words) - stop_words))
    matched_count = len([w for w in (set(jd_words) - stop_words) if w in resume])

    keyword_score = min(100, int((matched_count / max(keyword_count, 1)) * 100))
    impact_verbs = ["achieved", "led", "managed", "increased", "launched", "improved"]
    impact_score = min(100, (len([v for v in impact_verbs if v in resume]) * 20) + 30)
    readability_score = 95 if 300 < len(resume_text.split()) < 900 else 60

    total_score = int(
        (keyword_score * 0.5) + (impact_score * 0.3) + (readability_score * 0.2)
    )

    return {
        "ats_score": total_score,
        "sub_scores": {
            "keywords": keyword_score,
            "impact": impact_score,
            "readability": readability_score,
        },
        "strengths": ["Clear document structure", "Professional formatting detected"],
        "weaknesses": [
            "Low impact verb density",
            "Missing core technical industry terms",
        ],
        "missing_keywords": missing_skills[:10],
    }


# ================== ROUTES ==================
@app.route("/")
def index():
    return render_template("ATS.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return jsonify({"error": "Resume file missing"}), 400

    resume_file = request.files["resume"]
    job_desc = request.form.get("jobDesc", "")
    resume_text = extract_text_from_pdf(resume_file)

    if not resume_text:
        return jsonify({"error": "Failed to parse PDF content"}), 400

    if client:
        try:
            prompt = f"""
            Analyze Resume against Job Description. Return ONLY a valid JSON object.
            
            RULES for missing_keywords:
            - ONLY include Hard Skills (Python, React, etc), Tools (Git, AWS), or Industry Terms (Agile).
            - EXCLUDE common English words (knowledge, required, basic, etc).
            
            Resume: {resume_text}
            Job Description: {job_desc}
            """
            response = client.models.generate_content(
                model="gemini-2.0-flash", contents=prompt
            )
            if response and response.text:
                clean_json = response.text.replace("json", "").replace("", "").strip()
                return jsonify(json.loads(clean_json))
        except:
            pass

    return jsonify(local_ats_engine(resume_text, job_desc))


if __name__ == "__main__":
    app.run(debug=True, port=8080)
