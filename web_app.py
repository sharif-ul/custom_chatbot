from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

openai.api_key = "your-api-key-here"

def get_gpt3_response(prompt):
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7
    )
    return response.choices[0].text.strip()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.form["user_input"]
    response = get_gpt3_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
