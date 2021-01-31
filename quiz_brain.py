# TODO: 1. asking the questions
# TODO: 2. checking if the answer was correct
# TODO: 3. checking if we're at the end of the quiz

class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list
        self.score = 0

    def next_question(self):
        """Asks user next question from list of question objects, and calls check_answer method to see if user answer
        is correct"""
        q = self.list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {q.text} (True/False)?: ")
        correct_answer = q.answer

        self.check_answer(user_answer, correct_answer)

    def questions_left(self):
        """Returns True if there are questions left to ask, otherwise returns False"""
        return self.question_number < len(self.list)

    def check_answer(self, user_answer, correct_answer):
        """Increases quiz score if user entered correct answer"""
        possible_score = len(self.list)
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("Sorry, wrong answer")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")