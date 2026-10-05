# AI Personal Assistant

A Flask web app that uses the Google Gemini API to answer questions and summarize long emails.

## Features
- **Ask Anything:** get short, beginner-friendly answers to any question
- **Email Summarizer:** paste a long email and get a 2-3 sentence summary
- Real-time responses using the JavaScript Fetch API with loading indicators
- Task-specific prompts and tuned generation settings for each feature

## Tech Stack
Python, Flask, Gemini API, HTML, CSS, JavaScript

## Screenshots
[Add 1-2 screenshots here]

## Setup
1. Clone the repo:
   git clone https://github.com/vanshikagajul/AI-Personal-Assistant.git
   cd AI-Personal-Assistant
2. Install dependencies:
   pip install -r requirements.txt
3. Create a `.env` file in the project folder:
   GEMINI_API_KEY=your_api_key_here
4. Run the app:
   python main.py
5. Open http://127.0.0.1:5000 in your browser

## Project Structure
- `main.py`: Flask backend with the `/ask` and `/summarize` endpoints
- `templates/index.html`: frontend page
- `static/`: CSS styling

## Future Improvements
- Add error handling and input validation
- Add conversation history
- Deploy the app online
