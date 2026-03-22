from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.submitted_time = None

    def add_question(self, question):
        self.questions.append(question)

    def check_answer(self, user_answers):
        for i in range(len(self.questions)):
            if user_answers[i] == self.questions[i].answer:
                self.score += 1

        self.submitted_time = datetime.now()