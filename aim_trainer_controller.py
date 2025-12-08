"""
Controller for Aim Trainer
"""
import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEMOTION, QUIT, KEYDOWN, K_ESCAPE


class AimTrainerController:
    """
    Tracks and takes user input

    Attributes:
        _status: a instance
    """

    pygame.init()

    def __init__(self, status):
        """
        Saves instance
        """
        self._status = status

    def end_screen_check(self):
        """
        Checks to see if user wants to start another game by clicking on the screen

        Returns:
            a boolean dependent on choice
        """
        # check to see if player is trying to exit game
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                return True
        return False

    def choose_difficulty(self):
        """
        Takes player choice on difficulty by logging if player clicks on a position occupied by the difficulty text

        Returns:
            a string stating a difficulty
        """
        # Check to see what difficulty player chose
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if self._status.difficulty_boxes()[0].collidepoint(
                    pygame.mouse.get_pos()
                ):
                    return "easy"
                if self._status.difficulty_boxes()[1].collidepoint(
                    pygame.mouse.get_pos()
                ):
                    return "medium"
                if self._status.difficulty_boxes()[2].collidepoint(
                    pygame.mouse.get_pos()
                ):
                    return "hard"

        return None

    def mouse_pos(self):
        """
        Saves mouse position when mouse is clicked
        """
        if pygame.event.get == MOUSEMOTION:
            self._status.MOUSE_X = pygame.mouse.get_pos[0]
            self._status.MOUSE_Y = pygame.mouse.get_pos[1]

    def exit_program(self):
        """
        Checks if player is trying to escape or close game window and then closes it
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self._status.terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self._status.terminate()
