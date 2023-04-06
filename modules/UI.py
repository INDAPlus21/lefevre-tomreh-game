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
        """
        Initialize text object
        
        Args:
            text: string to be shown
            pos: position of text
            color: color of text
        """
        self.text = text
        self.rect = FONT.get_rect(text)
        self.rect.center = pos
        self.color = color

    def draw(self, surface):
        """
        Draw text object to screen.
        
        Args:
            surface: game window.
        """
        FONT.render_to(surface, self.rect, self.text, self.color)


class Button:
    def __init__(self, text, pos, color, hover=WHITE) -> None:
        """
        Initialize button object.
        
        Args:
            text: text on button.
            pos: position of button.
            color: color of button.
            hover: color when hovered over.
        """
        self.text = text
        self.rect = FONT.get_rect(text)
        self.rect.center = pos
        self.hover = hover
        self.color = color

    def is_hover(self):
        """
        If the mouse position is currently over the button
        
        Returns:
            bool: True if cursor is currently over the button, False otherwise.
        """
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def draw(self, surface):
        """
        Draw button object.
        
        Args:
            surface: game window.
        """
        if self.is_hover():
            FONT.render_to(surface, self.rect, self.text, self.hover)
        else:
            FONT.render_to(surface, self.rect, self.text, self.color)


class MainMenu:
    def __init__(self, surface) -> None:
        """
        Initialize mainmenu object.
        
        Args:
            surface: game window.
        """
        x, y = surface.get_size()
        self.snake_text = Text("PvSnake", (x//2, y//4), WHITE)
        self.buttonPlayer = Button("1 Player", (x//4, y//1.7), BLUE)
        self.buttonBot = Button("1 Bot", (3*x//4, y//1.7), BLUE)
        self.buttonPlayerVSPlayer = Button("PvP", (0.5*x//6, y//1.3), RED)
        self.buttonPlayerVSBot = Button("PvBot", (2.5*x//6, y//1.3), RED)
        self.buttonBotVSBot = Button("BotvBot", (5*x//6, y//1.3), RED)


    def run(self, surface, events):
        """
        Run mainmenu object.
        
        Args:
            surface: game window.
            events: list of events.
        
        Returns:
            Scene: new scene state.
        """
        click_flag = False
        state = Scene.MAINMENU

        # Handle events
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_flag = True

        # Draw scene
        self.draw(surface)

        # If left mouse button was clicked, check if any button was clicked
        if(click_flag):
            state = self.clicked_button(state)

        pygame.display.flip()

        return state
    

    def draw(self, surface):
        """
        Draw scene onto the game window.
        
        Args:
            surface: game window.
        """
        surface.fill((0, 0, 0))
        self.snake_text.draw(surface)
        self.buttonPlayer.draw(surface)
        self.buttonBot.draw(surface)
        self.buttonPlayerVSPlayer.draw(surface)
        self.buttonPlayerVSBot.draw(surface)
        self.buttonBotVSBot.draw(surface)


    def clicked_button(self, state):
        """
        Check if mouse has clicked any button.

        Args:
            state: current game scene state.
        """
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

        return state


class EndScreen:
    def __init__(self, surface: pygame.surface.Surface) -> None:
        """
        Initialize game over screen.
        
        Args: 
            surface: game window.
        """
        x, y = surface.get_size()
        self.play_again = Button("Play again", (x//2, 3*y//4), WHITE, BLUE)


    def run(self, surface, events, loser):
        """
        Run game over scene
        
        Args:
            surface: game window.
            events: list of events.
            loser: losing snake of previous game.
        
        Returns:
            Scene: new scene state.
        """
        click_flag = False
        state = Scene.GAMEOVER

        # Handle events
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                click_flag = True

        # Determine game over message
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

        # Print scene to game window
        surface.fill((0, 0, 0))
        self.play_again.draw(surface)
        text.draw(surface)

        # Change scene state if main menu button was clicked
        if click_flag and self.play_again.is_hover():
            state = Scene.MAINMENU

        pygame.display.flip()

        return state


class UI:
    def __init__(self, surface) -> None:
        """
        Initialize UI elements.
        
        Args:
            surface: game window.
        """
        self.menu = MainMenu(surface)
        self.end = EndScreen(surface)
