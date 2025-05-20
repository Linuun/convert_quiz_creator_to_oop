# set a class responsible for saving the quiz questions to a file
from QuizBase import QuizBase
class FileSaver(QuizBase):
    def save_to_file(self, questions_data):
# open the file in append mode and write the questions and answers