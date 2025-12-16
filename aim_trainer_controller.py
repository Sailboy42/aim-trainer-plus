"""
User input handling for aim trainer.

Responsibilities:
- Capture and process mouse events (clicks, motion)
- Detect difficulty selection from button clicks
- Handle exit signals (window close, ESC key)
- Update game state based on user input
"""

import pygame
from pygame import MOUSEBUTTONDOWN, MOUSEMOTION, QUIT, KEYDOWN, K_ESCAPE


class AimTrainerController:
    """
    Controller component managing user input and game control flow.

    Translates pygame events into game actions through the Range model.
    Handles difficulty selection, mouse tracking, and exit conditions.

    Attributes:
        _status: Reference to AimTrainerRange (Model) instance
    """

    pygame.init()

    def __init__(self, status):
        """Initialize controller with reference to game model."""
        self._status = status

    # ==================== Difficulty Selection ====================

    def choose_difficulty(self):
        """
        Detect difficulty button clicks and return selected difficulty.

        Checks mouse clicks against three difficulty button areas:
        - Button 0 (left): Easy
        - Button 1 (center): Medium
        - Button 2 (right): Hard

        Returns:
            "easy", "medium", "hard" if button clicked, None otherwise
        """
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                boxes = self._status.difficulty_boxes()
                if boxes[0].collidepoint(pygame.mouse.get_pos()):
                    return "easy"
                if boxes[1].collidepoint(pygame.mouse.get_pos()):
                    return "medium"
                if boxes[2].collidepoint(pygame.mouse.get_pos()):
                    return "hard"
        return None

    def detect_difficulty_selection(self, mouse_pos):
        """
        Check if mouse position overlaps with any difficulty button.

        Args:
            mouse_pos: Tuple (x, y) of mouse position

        Returns:
            Difficulty string if button hit, None otherwise
        """
        boxes = self._status.difficulty_boxes()
        if boxes[0].collidepoint(mouse_pos):
            return "easy"
        if boxes[1].collidepoint(mouse_pos):
            return "medium"
        if boxes[2].collidepoint(mouse_pos):
            return "hard"
        return None

    # ==================== Mouse Tracking ====================

    def mouse_pos(self):
        """
        Update game model with current mouse position.

        Tracks MOUSEMOTION events and stores position in model.
        """
        for event in pygame.event.get():
            if event.type == MOUSEMOTION:
                pos = pygame.mouse.get_pos()
                self._status._MOUSE_X = pos[0]
                self._status._MOUSE_Y = pos[1]

    def get_mouse_position_from_event(self, event):
        """
        Extract mouse position from a pygame event.

        Args:
            event: pygame.event.Event object

        Returns:
            Tuple (x, y) if event has position, None otherwise
        """
        return event.dict.get("pos")

    # ==================== Exit Handling ====================

    def exit_program(self):
        """
        Check for exit signals and terminate if detected.

        Exit signals:
        - Window close button (QUIT event)
        - ESC key press (KEYDOWN with K_ESCAPE)
        """
        for event in pygame.event.get():
            if event.type == QUIT:
                self._status.terminate()
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                self._status.terminate()

    def handle_quit_event(self, event):
        """
        Check if single event is a quit signal.

        Args:
            event: pygame.event.Event to check

        Returns:
            True if event is quit or ESC, False otherwise
        """
        if event.type == QUIT:
            return True
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            return True
        return False

    # ==================== Game Flow Control ====================

    def end_screen_check(self):
        """
        Detect if user wants to restart game from end screen.

        Checks for any mouse click to restart.

        Returns:
            True if click detected, False otherwise
        """
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                return True
        return False
