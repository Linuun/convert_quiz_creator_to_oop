# set a class responsible for the user interface functions like text box and background
# copy the code of user interface from the previous code
from QuizBase2 import QuizBase
import pygame
class QuizUI(QuizBase):
    def draw_text_box(self, surface, text, font, color, x, y, width, padding=10, bg_color=(40, 40, 60), border_radius=12):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x + padding, y + padding)
        box_rect = pygame.Rect(x, y, width, text_rect.height + 2 * padding)
        pygame.draw.rect(surface, bg_color, box_rect, border_radius=border_radius)
        surface.blit(text_surface, text_rect)
        return box_rect.bottom

    def draw_gradient(self, surface, color_top, color_bottom):
        for y in range(surface.get_height()):
            ratio = y / surface.get_height()
            red = int(color_top[0] * (1 - ratio) + color_bottom[0] * ratio)
            green = int(color_top[1] * (1 - ratio) + color_bottom[1] * ratio)
            blue = int(color_top[2] * (1 - ratio) + color_bottom[2] * ratio)
            pygame.draw.line(surface, (red, green, blue), (0, y), (surface.get_width(), y))