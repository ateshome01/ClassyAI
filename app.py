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
    user_courses = data.get("courses", [])

    # Filter professors that match classes
    matches = [p for p in professors if p["course"] in user_courses]

    # If no match found
    if not matches:
        return jsonify({"error": "No professors found for those classes"}), 400

    # Sort best → worst
    ranked = sorted(matches, key=lambda x: x["rating"], reverse=True)

    # AI explanation
    prompt = f"Explain why these professors are recommended: {ranked}"

    ai_response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You explain professor recommendations."},
            {"role": "user", "content": prompt}
        ]
    )

    explanation = ai_response.choices[0].message.content

    return jsonify({
        "ranked_professors": ranked,
        "ai_explanation": explanation
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
