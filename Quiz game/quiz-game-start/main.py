# Import the Classes , and data .
from question_model import Question
from data import question_data
from quiz_brain import  QuizBrain


# Take the question_data , and create from him a question_bank . 
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # Create a new instance of the Question Class .

    new_question = Question(question_text , question_answer)
    question_bank.append(new_question)


new_quiz = QuizBrain(question_bank)

while new_quiz.still_have_game():
    new_quiz.next_question()


print("You've completed the quiz")
print(f"Your final score was: {new_quiz.score}/{new_quiz.question_number}")
