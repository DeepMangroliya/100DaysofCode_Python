class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0


    def next_question(self):
        current_question = self.question_list[self.question_number]
        # print(current_question)
        self.question_number += 1
        # question_text = current_question.text
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        return self.check_answer(user_answer, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self,user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's incorrect!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score: {self.score}/{self.question_number}")
        print("\n")
