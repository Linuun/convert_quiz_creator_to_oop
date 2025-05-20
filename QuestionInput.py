# class responsible for taking user input for questions
from QuizBase import QuizBase
class QuestionInput(QuizBase):
    def get_question(self):
        print("\n⚒️ Let's build a fun quiz!")
# ask user to input a question, the possible answers, and the correct answer
        question = input(f"{self.GREEN}Enter a question: {self.RESET}")
        answer_a = input(f"{self.BLUE}A.) {self.RESET}")
        answer_b = input(f"{self.BLUE}B.) {self.RESET}")
        answer_c = input(f"{self.BLUE}C.) {self.RESET}")
        answer_d = input(f"{self.BLUE}D.) {self.RESET}")
        correct_answer = input("Enter the correct answer (A/B/C/D): ").upper()
# validate the correct answer
# return all question data as a dictionary