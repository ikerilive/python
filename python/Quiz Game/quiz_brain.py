class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.current_score = 0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        while True:
            user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
            if user_answer.lower() in ["true", "false"]:
                break
            else:
                print("Invalid input. Please enter 'True' or 'False'.")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.current_score += 1
            print("You got it right!")
        else:
            print("You got it wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.current_score}/{self.question_number}")
        print("\n")

