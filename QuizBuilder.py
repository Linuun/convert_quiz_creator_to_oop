# set a class the combines both question input and file saving logic
from QuestionInput import QuestionInput
from FileSaver import FileSaver
class QuizBuilder(QuestionInput, FileSaver):
    def run(self):
# use while loop
# ask the user to input a question
        while True:
            questions_data = self.get_question()
# save the question if input is valid
            if questions_data:
                self.save_to_file(questions_data)
# ask the user if they want to add another question
            again = input("Do you want to add another question? (YES/NO): ").upper()
# break the loop if they say no
            if again != "YES":
                print(f"\n{self.CYAN}🛠️ All done! You've built a fun and exciting quiz.🛠️{self.RESET}")
                print(f"\n{self.CYAN} All your questions have been saved in {self.file_name}.{self.RESET}")
                break