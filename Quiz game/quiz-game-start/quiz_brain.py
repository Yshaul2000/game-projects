# TODO: asking the questions
# TODO: checking if it's right .
# TODO: checking if the game need to finish .

class QuizBrain:
 
    def __init__(self , q_list):
        """ Counstructor ."""
        self.question_number  = 0
        self.question_list = q_list
        self.score = 0
    

    def next_question(self):
        """ Retrieve the item , and the number of the current question """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number}: {current_question.text} (True/False): ")


    def check_answer(self, user_answer, correct_answer):
        # If have small and cpital letters all will be small .

        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")


    def still_have_game(self):
        """ If the current question is < from the number of the last question the game will continue . """
        return self.question_number < len(self.question_list)