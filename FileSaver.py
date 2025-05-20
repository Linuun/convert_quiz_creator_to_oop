# set a class responsible for saving the quiz questions to a file
from QuizBase import QuizBase
class FileSaver(QuizBase):
    def save_to_file(self, questions_data):
# open the file in append mode and write the questions and answers
        with open(self.file_name, "a") as file:
            file.write(f"Question: {questions_data['question']}\n")
            file.write(f"A.) {questions_data['A']}\n")
            file.write(f"B.) {questions_data['B']}\n")
            file.write(f"C.) {questions_data['C']}\n")
            file.write(f"D.) {questions_data['D']}\n")
            file.write(f"The correct answer is: {questions_data['correct']}\n")
            file.write(f"=======================\n")

