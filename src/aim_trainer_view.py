"""
User interface rendering for aim trainer.

Responsibilities:
- Load and display background images
- Render game state (score, time, targets)
- Display difficulty selection screen
- Show endgame statistics screen
"""

import os
import pygame


class AimTrainerView:
    """
    View component managing all game rendering and UI display.

    Displays game state from model, renders backgrounds, text, targets,
    and UI elements. Coordinates visual feedback for all game screens.

    Attributes:
        FONT: Default font for UI text (48px)
        start_bg_raw: Raw start screen background image
        end_bg_raw: Raw end screen background image
        range_bg_raw: Raw gameplay background image
        _status: Reference to AimTrainerRange (Model) instance
        _start_bg: Scaled start screen background
        _end_bg: Scaled end screen background
        _range_bg: Scaled gameplay background
    """

    pygame.init()

    # Get assets directory path
    ASSETS_DIR = os.path.join(
        os.path.dirname(os.path.dirname(__file__)), "assets"
    )

    # Fonts
    FONT = pygame.font.SysFont("cs_regular.ttf", 48)
    FONT_DEFAULT = pygame.font.SysFont("cs_regular.ttf", 48)
    FONT_LARGE = pygame.font.SysFont("cs_regular.ttf", 72)
    FONT_XLARGE = pygame.font.SysFont("cs_regular.ttf", 112)

    # Background images
    start_bg_raw = pygame.image.load(
        os.path.join(ASSETS_DIR, "range-start.png")
    )
    end_bg_raw = pygame.image.load(os.path.join(ASSETS_DIR, "range-end.png"))
    range_bg_raw = pygame.image.load(os.path.join(ASSETS_DIR, "range2.png"))

    def __init__(self, status):
        """Initialize view with reference to game model and scale backgrounds."""
        self._status = status

        # Scale backgrounds to window dimensions
        window_size = (status.WINDOW_WIDTH, status.WINDOW_HEIGHT)
        self._start_bg = pygame.transform.scale(self.start_bg_raw, window_size)
        self._end_bg = pygame.transform.scale(self.end_bg_raw, window_size)
        self._range_bg = pygame.transform.scale(self.range_bg_raw, window_size)

    # ==================== Text Rendering ====================

    def draw_text(self, text, surface, x, y, font=None, color=None):
        """
        Render and blit text to surface at specified position.

        Args:
            text: String to render
            surface: pygame.Surface to draw on
            x: X coordinate for top-left of text
            y: Y coordinate for top-left of text
            font: pygame.font.Font (defaults to FONT)
            color: RGB tuple (defaults to RED)
        """
        if font is None:
            font = self.FONT
        if color is None:
            color = self._status.COLORS["RED"]

        text_object = font.render(text, 1, color)
        text_rect = text_object.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_object, text_rect)

    def render_text(self, text, font, color):
        """
        Render text to surface without blitting.

        Args:
            text: String to render
            font: pygame.font.Font for rendering
            color: RGB tuple for text color

        Returns:
            pygame.Surface containing rendered text
        """
        return font.render(text, 1, color)

    def blit_text(self, surface, text_surface, x, y):
        """
        Draw pre-rendered text surface to target surface.

        Args:
            surface: Target pygame.Surface
            text_surface: Pre-rendered text Surface
            x: X coordinate
            y: Y coordinate
        """
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        surface.blit(text_surface, text_rect)

    # ==================== Screen Rendering ====================

    def start_screen(self):
        """
        Display difficulty selection screen.

        Shows:
        - Background image
        - "Pick a difficulty" title
        - Three difficulty buttons (Easy, Medium, Hard)
        """
        self._status.window_surface.blit(self._start_bg, (0, 0))

        # Draw difficulty selection buttons
        boxes = self._status.difficulty_boxes()
        for box in boxes:
            pygame.draw.rect(
                self._status.window_surface, self._status.COLORS["RED"], box
            )

        # Title
        self.draw_text(
            "Pick a difficulty",
            self._status.window_surface,
            90,
            150,
            self.FONT_XLARGE,
        )

        # Button labels
        self.draw_text(
            "Easy",
            self._status.window_surface,
            83,
            485,
            self.FONT,
            self._status.COLORS["BLACK"],
        )
        self.draw_text(
            "Medium",
            self._status.window_surface,
            312,
            485,
            self.FONT,
            self._status.COLORS["BLACK"],
        )
        self.draw_text(
            "Hard",
            self._status.window_surface,
            580,
            485,
            self.FONT,
            self._status.COLORS["BLACK"],
        )

    def game_background(self):
        """Display gameplay background image."""
        self._status.window_surface.blit(self._range_bg, (0, 0))

    def game_status(self):
        """
        Display in-game HUD (score and time remaining).

        Shows:
        - Time remaining (top-left)
        - Current score (below time)
        """
        # Display time remaining
        self.draw_text(
            f"Time: {self._status.config()[0]}",
            self._status.window_surface,
            8,
            8,
        )

        # Display current score
        self.draw_text(
            f"Score: {self._status.score()}",
            self._status.window_surface,
            8,
            38,
        )

    def display_targets(self):
        """
        Render all active targets on gameplay screen.

        Blits target image at each target's position.
        """
        target_image = self._status.resize_target()
        for target in self._status.targets():
            self._status.window_surface.blit(target_image, target)

    def draw_game_stats(self, surface):
        """
        Render in-game statistics for debugging/display.

        Args:
            surface: pygame.Surface to draw on
        """
        stats = f"Score: {self._status.score()} | Targets: {len(self._status.targets())}"
        self.draw_text(stats, surface, 300, 8)

    def endgame_screen(self):
        """
        Display end game screen with final statistics.

        Shows:
        - "GAME OVER" title
        - Player accuracy percentage
        - Final score
        - Restart prompt
        """
        self._status.window_surface.blit(self._end_bg, (0, 0))
        self._status.window_surface.fill(self._status.COLORS["BLACK"])

        # Game over title
        self.draw_text(
            "GAME OVER",
            self._status.window_surface,
            200,
            325,
            self.FONT_LARGE,
        )

        # Restart prompt
        self.draw_text(
            "Click anywhere to restart",
            self._status.window_surface,
            170,
            380,
        )

        # Accuracy
        self.draw_text(
            f"Accuracy: {self._status.accuracy()}%",
            self._status.window_surface,
            269,
            414,
        )

        # Final score
        self.draw_text(
            f"Score: {self._status.score()}",
            self._status.window_surface,
            308,
            450,
        )

    def draw_difficulty_buttons(self, surface):
        """
        Draw difficulty selection buttons on surface.

        Args:
            surface: pygame.Surface to draw on
        """
        boxes = self._status.difficulty_boxes()
        for box in boxes:
            pygame.draw.rect(surface, self._status.COLORS["RED"], box)

    def draw_endgame_stats(self, surface):
        """
        Draw endgame statistics on surface.

        Args:
            surface: pygame.Surface to draw on
        """
        self.draw_text(
            f"Accuracy: {self._status.accuracy()}%",
            surface,
            269,
            414,
        )
        self.draw_text(
            f"Score: {self._status.score()}",
            surface,
            308,
            450,
        )
