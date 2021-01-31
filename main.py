import html
from data import get_questions
from question_model import Question
from quiz_brain import QuizBrain

difficulty = input("Choose your level(easy/medium/hard): ")
question_data = get_questions(difficulty)
question_bank = [Question(text=html.unescape(q['question']), answer=q['correct_answer']) for q in question_data]

host = QuizBrain(question_bank)

while host.questions_left():
    host.next_question()
    print("\n")

print("You've completed the quiz!")
print(f"Your final score was {host.score}/{host.question_number}")