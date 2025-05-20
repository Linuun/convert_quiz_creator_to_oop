# class that defines shared attributes like color codes and file name
# constructor that sets the file name 
class QuizBase:
    RED = '\033[91m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    RESET = '\033[0m'

    def __init__(self, file_name="quiz.txt"):
        self.file_name = file_name