# class responsible for taking user input for questions
from QuizBase import QuizBase
class QuestionInput(QuizBase):
    def get_question(self):
        print("\n⚒️ Let's build a fun quiz!")
# ask user to input a question, the possible answers, and the correct answer
# validate the correct answer
# return all question data as a dictionary