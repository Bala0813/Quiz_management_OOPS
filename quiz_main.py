from question_model import Question
from data import question_data
from Quiz_brain import Quiz_brain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz_brain(question_bank)
while quiz.process_question_list():
    quiz.next_question()

print(f"You've completed the quiz, your final score is {quiz.current_score}/{len(question_bank)}")
