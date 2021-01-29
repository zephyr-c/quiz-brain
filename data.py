import requests
TRIVIA_URL = "https://opentdb.com/api.php?amount=10"


payload = {'category': 9, 'difficulty': 'easy', 'type': 'boolean'}
results = requests.get()

# question_data = [
#     {"category": "General Knowledge",
#      "type": "boolean",
#      "difficulty": "easy",
#      "question": "Gumbo is a stew that originated in Louisiana.",
#      "correct_answer": "True",
#      "incorrect_answers": ["False"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                                        "question": "It is automatically considered entrapment in the United States if the police sell you illegal substances without revealing themselves.",
#                                        "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "Bulls are attracted to the color red.", "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "You can legally drink alcohol while driving in Mississippi.", "correct_answer": "True",
#      "incorrect_answers": ["False"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#                                        "question": "On average, at least 1 person is killed by a drunk driver in the United States every hour.",
#                                        "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy", "question": "Pluto is a planet.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "Adolf Hitler was born in Australia. ", "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "Romanian belongs to the Romance language family, shared with French, Spanish, Portuguese and Italian. ",
#      "correct_answer": "True", "incorrect_answers": ["False"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "Dihydrogen Monoxide was banned due to health risks after being discovered in 1983 inside swimming pools and drinking water.",
#      "correct_answer": "False", "incorrect_answers": ["True"]},
#     {"category": "General Knowledge", "type": "boolean", "difficulty": "easy",
#      "question": "Scotland voted to become an independent country during the referendum from September 2014.",
#      "correct_answer": "False", "incorrect_answers": ["True"]}]
