from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import json
import os

app = Flask(__name__)
CORS(app)

# Load AI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Load professors file
with open("data/mock_professors.json", "r") as file:
    professors = json.load(file)


@app.route("/recommend", methods=["POST"])
def recommend():
    data = request.json

    user_university = data.get("university", "").strip()
    user_courses = data.get("courses", [])

    # Filter by university first
    uni_matches = [p for p in professors if p["university"].lower()
                   == user_university.lower()]

    if not uni_matches:
        return jsonify({"error": "No professors found for that university"}), 400

    # Now filter by courses *within* the matched university
    course_matches = [p for p in uni_matches if p["course"] in user_courses]

    if not course_matches:
        return jsonify({"error": "No professors found for those classes at this university"}), 400

    ranked = sorted(course_matches, key=lambda x: x["rating"], reverse=True)

    # AI explanation
    prompt = f"Explain why these professors at {user_university} are recommended: {ranked}"

    ai_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You explain professor recommendations."},
            {"role": "user", "content": prompt}
        ]
    )

    explanation = ai_response.choices[0].message.content  # FIXED

    return jsonify({
        "ranked_professors": ranked,
        "ai_explanation": explanation
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
