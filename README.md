# ClassyAI

A GMU November Hackathon Project

ClassyAI is a lightweight Flask-based backend + HTML/JS frontend tool that recommends the best professors for a student’s upcoming classes. Using a mock dataset of realistic professor ratings and an AI explanation generator, ClassyAI helps students build smarter schedules quickly.

⸻

🚀 Features

🔍 Professor Recommendation
	•	Enter classes (e.g., “CS 112”, “MATH 113”)
	•	Backend filters professors from a dataset
	•	Ranks them by rating, difficulty, and number of reviews

🤖 AI-Generated Explanation
	•	Uses the OpenAI API to explain why those professors were recommended
	•	Provides human-like reasoning in plain English

🗂 Mock Dataset Included
	•	30+ realistic professors
	•	Ratings, difficulty score, and review counts

🧪 API Endpoint
	•	POST /recommend
	•	Accepts JSON:
 " {
  "courses": ["CS 112", "MATH 113"]
}"
	•	Returns ranked professors + AI explanation

⸻

🧰 Tech Stack

Backend: Python, Flask, OpenAI API
Frontend: HTML, CSS, JavaScript
Dataset: JSON (mock_professors.json)
Tools: Thunder Client / Postman for testing

📁 Project Structure
/Hackathon Project
│── app.py                 # Flask backend + AI integration
│── requirements.txt       # Python dependencies
│── index.html             # Simple frontend
│── /data
│     └── mock_professors.json
│── README.md              # (this file)
│── .gitignore             # prevents venv from uploading

▶️ How to Run the Backend (Local)
1. Install dependencies
   pip install -r requirements.txt
2. Set your OpenAI API Key
Mac/Linux:
export OPENAI_API_KEY=your-key-here
Windows CMD:
set OPENAI_API_KEY=your-key-here

3. Start the server
   python app.py

   The backend runs at:
http://localhost:5000

⸻

⚡ Testing the API (Thunder Client)
	1.	Open VS Code → Thunder Client
	2.	Click New Request
	3.	Set method to POST
	4.	URL: http://localhost:5000/recommend
  5.	Click Body → JSON
	6.	Paste: {
  "courses": ["CS 112", "MATH 113"]
}
  7.	Send → You get ranked professors + explanation.

🎨 Frontend

The frontend (index.html) allows students to:
	•	Enter classes
	•	Click “Generate Recommendations”
	•	Display ranked professors + AI explanation

Uses simple fetch() calls to connect to the backend.

⸻

👥 Team Roles

Backend
	•	Flask API
	•	Professor dataset
	•	Ranking logic
	•	OpenAI for explanations
	•	Endpoint with Thunder Client

Frontend
	•	HTML/CSS/JS UI
	•	Fetch() request to backend
	•	Output & layout

Dataset + UX
	•	mock_professors.json
	•	UI text, tested flows

⸻

🏁 Future Improvements
	•	Real RateMyProfessors scraping
	•	Real class scheduling integration
	•	Login system
	•	Save favorite professors
	•	Graphical dashboard

⸻

📜 License

MIT License
Free to use, modify, and expand.
