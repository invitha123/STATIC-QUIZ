from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample quiz data (replace with your questions and answers)
questions = [
    {"question": "What is the capital of France?", "answers": ["Paris", "London", "Berlin"], "correct_answer": 0},
    {"question": "What is the largest planet in our solar system?", "answers": ["Jupiter", "Earth", "Mars"], "correct_answer": 0},
    {"question": "Who wrote 'Romeo and Juliet'?", "answers": ["William Shakespeare", "Charles Dickens", "Jane Austen"], "correct_answer": 0},
    {"question": "What is the chemical symbol for water?", "answers": ["H2O", "CO2", "NaCl"], "correct_answer": 0}
]

# Global variables to track the current question index and score
current_question_index = 0
score = 0

@app.route("/", methods=["GET", "POST"])
def welcome():
    return render_template("welcome.html")

@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    global current_question_index, score
    if request.method == "POST":
        user_answer = int(request.form["answer"])
        if user_answer == questions[current_question_index]["correct_answer"]:
            score += 1
            message = "Correct!"
        else:
            message = f"Incorrect. The correct answer is {questions[current_question_index]['answers'][questions[current_question_index]['correct_answer']]}."
        current_question_index += 1
    else:
        message = ""

    if current_question_index == len(questions):
        return redirect(url_for("quiz_completed"))

    return render_template("quiz1.html", question=questions[current_question_index], message=message)

@app.route("/quiz_completed")
def quiz_completed():
    global current_question_index, score
    return render_template("quiz2.html", score=score, total_questions=len(questions))

if __name__ == "__main__":
    app.run(debug=True)

