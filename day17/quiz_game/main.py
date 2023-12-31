from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for question in question_data:
    x = Question(question["text"], question["answer"])
    question_bank.append(x)
quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(f"You have completed the quiz. Your total score is {quiz.score}/{quiz.question_number}")

