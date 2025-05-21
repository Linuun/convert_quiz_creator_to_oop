# set a class responsible for loading questions from a quiz file
# copy the code of loading questions from previous project
from QuizBase2 import QuizBase
class QuizLoader(QuizBase):
    def load_questions(self, file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            content = file.read().strip()
        question_blocks = content.split('=======================')
        questions = []

        for block in question_blocks:
            lines = block.strip().split('\n')
            if len(lines) < 6:
                continue

            question_line = lines[0]
            choices_lines = lines[1:5]
            answer_line = lines[5]

            if not question_line.startswith("Question:"):
                continue

            question = question_line[len("Question:"):].strip()
            choices = [line[4:].strip() for line in choices_lines if len(line) > 3 and line[1:4] == '.) ']
            answer_letter = answer_line.split(":")[-1].strip()
            correct_index = ord(answer_letter.upper()) - ord('A')
            if 0 <= correct_index < len(choices):
                correct_answer = choices[correct_index]
                questions.append((question, choices, correct_answer))

        return questions
