import pygame
import pygame.freetype
import sys
from modules.scenes import Scene

pygame.freetype.init()
FONT = pygame.freetype.Font('assets/Minecraft.ttf', 32)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)


class Text:
    def __init__(self, text, pos, color) -> None:
        self.text = text
        self.rect = FONT.get_rect(text)
        self.rect.center = pos
        self.color = color

    def draw(self, surface):
        FONT.render_to(surface, self.rect, self.text, self.color)


class Button:
    def __init__(self, text, pos, color, hover=WHITE) -> None:
        self.text = text
        self.rect = FONT.get_rect(text)
        self.rect.center = pos
        self.hover = hover
        self.color = color

    def is_hover(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface):
        if self.is_hover():
            FONT.render_to(surface, self.rect, self.text, self.hover)
        else:
            FONT.render_to(surface, self.rect, self.text, self.color)


class MainMenu:
    def __init__(self, surface) -> None:
        x, y = surface.get_size()
        self.snake_text = Text("PvSnake", (x//2, y//4), WHITE)
        self.buttonPlayer = Button("1 Player", (x//4, y//1.7), BLUE)
        self.buttonBot = Button("1 Bot", (3*x//4, y//1.7), BLUE)
        self.buttonPlayerVSPlayer = Button("PvP", (0.5*x//6, y//1.3), RED)
        self.buttonPlayerVSBot = Button("PvBot", (2.5*x//6, y//1.3), RED)
        self.buttonBotVSBot = Button("BotvBot", (5*x//6, y//1.3), RED)

    def run(self, surface, events):
        click_flag = False
        state = Scene.MAINMENU

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_flag = True

        surface.fill((0, 0, 0))
        self.snake_text.draw(surface)
        self.buttonPlayer.draw(surface)
        self.buttonBot.draw(surface)
        self.buttonPlayerVSPlayer.draw(surface)
        self.buttonPlayerVSBot.draw(surface)
        self.buttonBotVSBot.draw(surface)

        if click_flag:
            if self.buttonPlayer.is_hover():
                state = Scene.SINGLEPLAYER
            elif self.buttonBot.is_hover():
                state = Scene.SINGLEPLAYER_BOT
            elif self.buttonPlayerVSPlayer.is_hover():
                state = Scene.MULTIPLAYER
            elif self.buttonPlayerVSBot.is_hover():
                state = Scene.MULTIPLAYER_BOT
            elif self.buttonBotVSBot.is_hover():
                state = Scene.MULTIPLAYER_2BOT

        pygame.display.flip()

        return state


class EndScreen:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        x, y = surface.get_size()
        self.play_again = Button("Play again", (x//2, 3*y//4), WHITE, BLUE)

    def run(self, surface, events, loser):
        click_flag = False
        state = Scene.GAMEOVER

        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_flag = True

        x, y = surface.get_size()
        pos = (x//2, y//4)
        match loser:
            case 0:
                text = Text("Blue snake lost!", pos, BLUE)
            case 1:
                text = Text("Red snake lost!", pos, RED)
            case 2:
                text = Text("Draw!", pos, WHITE)
            case _:
                text = Text("???", pos, WHITE)

        surface.fill((0, 0, 0))
        self.play_again.draw(surface)
        text.draw(surface)

        if click_flag and self.play_again.is_hover():
            state = Scene.MAINMENU

        pygame.display.flip()

        return state


class UI:
    def __init__(self, surface) -> None:
        self.menu = MainMenu(surface)
        self.end = EndScreen(surface)
