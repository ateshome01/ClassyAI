<!-- f041f316-f1f1-4b13-8ac4-ee5f0ce926d6 c707f38f-ee24-4f87-a365-aa16fed91a06 -->
# Professor Chatbot Prototype

Build a conversational chatbot that helps users find top-rated professors by university and class using a mock dataset.

## Architecture

- **Frontend**: HTML with JavaScript for conversational chat interface
- **Backend**: Python Flask server with REST API endpoints
- **Data**: Mock professor dataset stored in JSON format

## Implementation Details

### Backend (Python/Flask)

- `app.py`: Main Flask application with chat endpoint
- `data/mock_professors.json`: Mock dataset containing:
- Universities
- Classes (exact course names)
- Professors with ratings, difficulty, and reviews
- Logic to filter professors by university and class (exact match)
- Sort by rating and return top 3 professors

### Frontend (HTML/JavaScript)

- `index.html`: Chat interface with:
- Message display area
- Input field for user messages
- Send button
- Styling for conversational UI
- JavaScript to:
- Send messages to backend API
- Display bot responses
- Handle conversation flow (greeting, collect university, collect class, show results)

### Key Features

- Conversational flow: Greet → Ask for university → Ask for class → Display top 3 professors
- Exact class name matching
- Mock data includes realistic professor ratings, difficulty scores, and sample reviews
- Clean, modern chat UI

## Files to Create

1. `data/mock_professors.json` - Mock professor dataset
2. `app.py` - Flask backend server
3. `index.html` - Chat interface frontend
4. `requirements.txt` - Python dependencies (Flask, flask-cors)
5. `README.md` - Setup and usage instructions

## Implementation Order

1. **Create mock data first** - Foundation for everything else
2. **Build backend API** - Test independently using tools like Postman/curl to verify it returns correct data
3. **Build frontend** - Connect to backend API from the start (JavaScript fetch calls)
4. **Test integration** - Run Flask server and open HTML in browser to test full flow

**When to bridge**: Connect frontend to backend immediately when building the frontend (step 3). The JavaScript will make API calls to the Flask server, so they need to work together from the start. You can test the backend API separately first (step 2) before building the frontend.

### To-dos

- [ ] Create mock_professors.json with sample universities, classes, and professors with ratings
- [ ] Build Flask app.py with chat endpoint that processes university/class queries and returns top 3 professors
- [ ] Build index.html with conversational chat interface and JavaScript for API communication
- [ ] Create requirements.txt with Flask and flask-cors dependencies