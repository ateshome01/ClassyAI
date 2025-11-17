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
    uni_name = data.get("university")  # University name from frontend
    user_courses = data.get("courses", [])  # List of courses

    matches = []

    if uni_name and uni_name in professors["universities"]:
        uni_courses = professors["universities"][uni_name]
        for course_name in user_courses:
            if course_name in uni_courses:
                for prof in uni_courses[course_name]:
                    prof_copy = prof.copy()
                    prof_copy["course"] = course_name
                    prof_copy["university"] = uni_name
                    matches.append(prof_copy)

    if not matches:
        return jsonify({"error": "No professors found for those classes"}), 400

    # Sort professors by rating (highest first)
    ranked = sorted(matches, key=lambda x: x["rating"], reverse=True)

    # AI explanation prompt
    prompt = f"Explain why these professors are recommended: {ranked}"

    ai_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You explain professor recommendations."},
            {"role": "user", "content": prompt}
        ]
    )

    explanation = getattr(ai_response.choices[0].message, "content", "")

    return jsonify({
        "ranked_professors": ranked,
        "ai_explanation": explanation
    })





if __name__ == "__main__":
    app.run(port=5000, debug=True)
