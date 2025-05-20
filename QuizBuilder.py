# set a class the combines both question input and file saving logic
from QuestionInput import QuestionInput
from FileSaver import FileSaver
class QuizBuilder(QuestionInput, FileSaver):
    def run(self):
# use while loop
# ask the user to input a question
# save the question if input is valid
# ask the user if they want to add another question
# break the loop if they say no