from flask import Flask,render_template,request , jsonify
import os
from dotenv import load_dotenv
from google import genai

app = Flask(__name__)

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

@app.route("/")
def hello_world():
    return render_template("index.html")

  

@app.route("/ask", methods=["POST"])
def ask():
    question = request.form.get("question", "").strip()

    if not question:
        return jsonify({"response": "Please enter a question."}), 400

    response = client.interactions.create(
        model="gemini-3.8-flash",
        system_instruction=(
            "You are a helpful AI personal assistant. "
            "Answer the user's question completely but briefly. "
            "Use simple and beginner-friendly language. "
            "Give around 2 to 4 sentences. "
            "Do not give unnecessary details."
        ),
        input=f"Answer this question completely and clearly: {question}",
        generation_config={
            "temperature": 0.7,
            "max_output_tokens": 512
        }
    )

    answer = response.output_text.strip()

    return jsonify({"response": answer}), 200



@app.route("/summarize", methods=["POST"])
def summarize():
    # Get email text from form data
    email_text = request.form.get("email" )

    prompt = f"Summarize the following email in 2-3 sentences: {email_text}"

    response = client.interactions.create(
        model="gemini-3.8-flash",
        system_instruction="Act like an expert email assistant",
        input=prompt,
        generation_config={
            "temperature": 0.3,
            "max_output_tokens": 512
        }
    )

    summary = response.output_text.strip()
    return jsonify({"response": summary}), 200


if __name__ == '__main__':
    app.run(debug=True)