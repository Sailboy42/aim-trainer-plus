"""
Controller for Aim Trainer
"""

import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEMOTION, QUIT, KEYDOWN, K_ESCAPE


def handle_quit_event(status):
    """
    Check and handle quit events (window close or ESC key).

    Args:
        status: AimTrainerRange instance
    """
    for event in pygame.event.get():
        if event.type == QUIT:
            status.terminate()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                status.terminate()


def get_mouse_position_from_event():
    """
    Get current mouse position from pygame events.

    Returns:
        tuple: (x, y) mouse coordinates
    """
    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            return pygame.mouse.get_pos()
    return None


def detect_difficulty_selection(status, mouse_pos):
    """
    Detect which difficulty button was clicked.

    Args:
        status: AimTrainerRange instance
        mouse_pos: tuple of (x, y) mouse coordinates

    Returns:
        str: difficulty level ("easy", "medium", "hard") or None
    """
    if mouse_pos is None:
        return None

    difficulty_boxes = status.difficulty_boxes()
    if difficulty_boxes[0].collidepoint(mouse_pos):
        return "easy"
    if difficulty_boxes[1].collidepoint(mouse_pos):
        return "medium"
    if difficulty_boxes[2].collidepoint(mouse_pos):
        return "hard"
    return None


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
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                difficulty = detect_difficulty_selection(
                    self._status, mouse_pos
                )
                if difficulty:
                    return difficulty
        return None

    def mouse_pos(self):
        """
        Saves mouse position when mouse is moved
        """
        mouse_position = get_mouse_position_from_event()
        if mouse_position:
            self._status.mouse_x = mouse_position[0]
            self._status.mouse_y = mouse_position[1]

    def exit_program(self):
        """
        Checks if player is trying to escape or close game window and then closes it
        """
        handle_quit_event(self._status)
