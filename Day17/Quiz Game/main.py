from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    question_bank.append(Question(question_text, question_answer))

quiz = QuizBrain(question_bank)

while (quiz.still_has_questions()):
    score = quiz.next_question()
    # score = quiz.check_answer(user_answer)
print(f"Your final score is: {quiz.score}")
print("Thank you for playing")
