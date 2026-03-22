Step 2 app py (flask backend )
from flask import Flask, render_template, request
from models import Question, Quiz

app = Flask(__name__)

quiz = Quiz()

# Add sample questions
quiz.add_question(Question("Capital of Nigeria?", ["Abuja", "Lagos", "Kano"], "Abuja"))
quiz.add_question(Question("2 + 2?", ["3", "4", "5"], "4"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/quiz")
def quiz_page():
    return render_template("quiz.html", questions=quiz.questions)

@app.route("/submit", methods=["POST"])
def submit():
    answers = []
    for i in range(len(quiz.questions)):
        answers.append(request.form.get(f"q{i}"))

    quiz.check_answer(answers)

    return render_template("result.html",
                           score=quiz.score,
                           total=len(quiz.questions),
                           time=quiz.submitted_time)

if __name__ == "__main__":
    app.run(debug=True)