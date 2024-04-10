from questionmodel import Question
from questiondata import question_data
from quizbrain import QuizBrain

question_bank =[]

for question in question_data:
    question_text =question["text"]
    question_answer =question["answer"]
    new_question =Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the Quiz")
print(f"The final score is {quiz.score} / {quiz.question_number}")
