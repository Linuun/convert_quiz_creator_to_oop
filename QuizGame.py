# set a class responsible for the main game logic
# copy the code of the main game loop from the previous code
from QuizLoader import QuizLoader
from QuizUI import QuizUI
import pygame
import sys
import random
class QuizGame(QuizLoader, QuizUI):
    def run(self):
        file = self.choose_quiz_file()
        if not file:
            print("No file selected.")
            sys.exit()

        questions = self.load_questions(file)
        if not questions:
            print("No valid questions found in the file.")
            sys.exit()

        self.run_quiz_game(questions)

    def run_quiz_game(self, questions):
        pygame.init()
        screen = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("Quiz Master")
        font = pygame.font.SysFont("arial", 28, bold=True)
        small_font = pygame.font.SysFont("arial", 22)
        clock = pygame.time.Clock()

        random.shuffle(questions)
        question_index = 0
        user_input = ""
        feedback = ""
        feedback_color = (255, 255, 255)
        score = 0
        game_over = False
        running = True

        while running:
            self.draw_gradient(screen, (15, 20, 45), (30, 60, 90))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if not game_over:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            correct_answer = questions[question_index][2]
                            selected_letter = user_input.strip().upper()
                            try:
                                selected_index = ord(selected_letter) - ord('A')
                                selected_answer = questions[question_index][1][selected_index]
                            except:
                                selected_answer = ""

                            if selected_answer == correct_answer:
                                feedback = "✅ Correct!"
                                feedback_color = (100, 255, 100)
                                score += 1
                            else:
                                feedback = f"❌ Incorrect! Correct: {correct_answer}"
                                feedback_color = (255, 100, 100)

                            user_input = ""
                            question_index += 1
                            if question_index >= len(questions):
                                game_over = True
                        elif event.key == pygame.K_BACKSPACE:
                            user_input = user_input[:-1]
                        elif event.unicode.isalpha():
                            user_input = event.unicode.upper()

            margin_top = 50
            margin_left = 60

            if not game_over:
                question = questions[question_index][0]
                choices = questions[question_index][1]

                y = self.draw_text_box(screen, f"Question {question_index + 1}", font, (255, 255, 255), margin_left, margin_top, 780)
                y = self.draw_text_box(screen, question, font, (255, 255, 0), margin_left, y + 20, 780)

                for i, choice in enumerate(choices):
                    y = self.draw_text_box(screen, f"{chr(65 + i)}) {choice}", small_font, (200, 200, 200), margin_left, y + 10, 780)

                y += 30
                self.draw_text_box(screen, f"Your Answer (A-D): {user_input}", small_font, (200, 200, 255), margin_left, y, 780)
                self.draw_text_box(screen, feedback, small_font, feedback_color, margin_left, y + 50, 780)
            else:
                y = self.draw_text_box(screen, "🎉 Quiz Complete!", font, (255, 255, 255), margin_left, margin_top, 780)
                y = self.draw_text_box(screen, f"Your score: {score} / {len(questions)}", font, (0, 255, 0), margin_left, y + 30, 780)
                self.draw_text_box(screen, "Press ESC to exit.", small_font, (180, 180, 180), margin_left, y + 60, 780)

                keys = pygame.key.get_pressed()
                if keys[pygame.K_ESCAPE]:
                    running = False

            pygame.display.flip()
            clock.tick(30)
        pygame.quit()