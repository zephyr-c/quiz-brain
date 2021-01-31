from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = [Question(q['question'], q['correct_answer']) for q in question_data]

host = QuizBrain(question_bank)

while host.questions_left():
    host.next_question()
    print("\n")

print("You've completed the quiz!")
print(f"Your final score was {host.score}/{host.question_number}")