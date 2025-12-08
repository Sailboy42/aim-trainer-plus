"""
View for Aim Trainer
"""

import pygame


def render_text(font, text, color):
    """
    Render text to a surface.

    Args:
        font: pygame.font.Font object
        text: Text string to render
        color: RGB color tuple

    Returns:
        pygame.Surface: Rendered text surface
    """
    return font.render(text, True, color)


def blit_text(surface, text_surface, x, y):
    """
    Draw rendered text surface at specified position.

    Args:
        surface: pygame.Surface target
        text_surface: Rendered text surface
        x: X coordinate
        y: Y coordinate
    """
    text_rect = text_surface.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_surface, text_rect)


def draw_difficulty_buttons(surface, colors, font_default):
    """
    Draw difficulty selection buttons.

    Args:
        surface: pygame.Surface target
        colors: Dictionary of color tuples
        font_default: Default font object
    """
    difficulty_boxes = [
        (pygame.Rect(5, 450, 240, 100), "Easy", 83, 485),
        (pygame.Rect(255, 450, 240, 100), "Medium", 312, 485),
        (pygame.Rect(505, 450, 240, 100), "Hard", 580, 485),
    ]

    for rect, label, x, y in difficulty_boxes:
        pygame.draw.rect(surface, colors["RED"], rect)
        text_surface = render_text(font_default, label, colors["BLACK"])
        blit_text(surface, text_surface, x, y)


def draw_game_stats(surface, time_remaining, score, font_default, colors):
    """
    Draw game status (time and score) during gameplay.

    Args:
        surface: pygame.Surface target
        time_remaining: Time left in game
        score: Current score
        font_default: Default font object
        colors: Dictionary of color tuples
    """
    time_text = render_text(
        font_default, f"Time: {time_remaining}", colors["RED"]
    )
    score_text = render_text(font_default, f"Score: {score}", colors["RED"])
    blit_text(surface, time_text, 8, 8)
    blit_text(surface, score_text, 8, 38)


def draw_endgame_stats(
    surface, accuracy, score, font_large, font_default, colors
):
    """
    Draw endgame statistics.

    Args:
        surface: pygame.Surface target
        accuracy: Player accuracy percentage
        score: Final score
        font_large: Large font object
        font_default: Default font object
        colors: Dictionary of color tuples
    """
    # Game over title
    game_over_text = render_text(font_large, "GAME OVER", colors["WHITE"])
    blit_text(surface, game_over_text, 200, 325)

    # Restart prompt
    restart_text = render_text(
        font_default, "Click anywhere to restart", colors["WHITE"]
    )
    blit_text(surface, restart_text, 170, 380)

    # Stats
    accuracy_text = render_text(
        font_default, f"Accuracy: {accuracy}%", colors["WHITE"]
    )
    score_text = render_text(font_default, f"Score: {score}", colors["WHITE"])
    blit_text(surface, accuracy_text, 269, 414)
    blit_text(surface, score_text, 308, 450)


class AimTrainerView:
    """
    Prompts text and images for aim trainer

    FONT_DEFAULT: default font for UI
    FONT_LARGE: large font for titles
    FONT_XLARGE: extra large font for game over
    start_bg_raw: raw start background image
    end_bg_raw: raw end background image
    range_bg_raw: raw game background image
    _status: reference to AimTrainerRange instance
    _start_bg: scaled start background
    _end_bg: scaled end background
    _range_bg: scaled game background
    """

    pygame.init()

    FONT_DEFAULT = pygame.font.Font(None, 48)
    FONT_LARGE = pygame.font.Font(None, 72)
    FONT_XLARGE = pygame.font.Font(None, 112)

    start_bg_raw = pygame.image.load("range-start.png")
    end_bg_raw = pygame.image.load("range-end.png")
    range_bg_raw = pygame.image.load("range2.png")

    def __init__(self, status):
        """ """
        self._status = status
        self._start_bg = pygame.transform.scale(
            self.start_bg_raw,
            (self._status.WINDOW_WIDTH, self._status.WINDOW_HEIGHT),
        )
        self._end_bg = pygame.transform.scale(
            self.end_bg_raw,
            (self._status.WINDOW_WIDTH, self._status.WINDOW_HEIGHT),
        )
        self._range_bg = pygame.transform.scale(
            self.range_bg_raw,
            (self._status.WINDOW_WIDTH, self._status.WINDOW_HEIGHT),
        )

    def draw_text(
        self, text, surface, x, y, font=None, color=None
    ):  # pylint: disable=too-many-arguments
        """
        Displays text on screen

        Args:
            text: The text to render
            surface: The pygame surface to draw on
            x: X coordinate for text placement
            y: Y coordinate for text placement
            font: Optional pygame font object (defaults to FONT_DEFAULT)
            color: Optional RGB color tuple (defaults to RED)
        """
        if font is None:
            font = self.FONT_DEFAULT
        if color is None:
            color = self._status.COLORS["RED"]
        # Load text
        text_object = font.render(text, 1, color)
        # get area of text
        text_rect = text_object.get_rect()
        # align text
        text_rect.topleft = (x, y)
        # display on surface
        surface.blit(text_object, text_rect)

    def endgame_screen(self):
        """
        Endgame text and final status and prompts user of next steps
        """
        self._status.window_surface.blit(self._end_bg, (0, 0))
        self._status.window_surface.fill(self._status.COLORS["BLACK"])
        draw_endgame_stats(
            self._status.window_surface,
            self._status.accuracy(),
            self._status.score(),
            self.FONT_LARGE,
            self.FONT_DEFAULT,
            self._status.COLORS,
        )
        pygame.display.update()

    def game_status(self):
        """
        Display time and score of ongoing game
        """
        draw_game_stats(
            self._status.window_surface,
            self._status.config()[0],
            self._status.score(),
            self.FONT_DEFAULT,
            self._status.COLORS,
        )

    def display_targets(self):
        """
        Spawn targets in cords of pre-made list
        """
        for target in self._status.resize_target():
            self._status.window_surface.blit(
                self._status.resize_target(), target
            )

    def game_background(self):
        """
        Set background to range image
        """
        self._status.window_surface.blit(self._range_bg, (0, 0))

    def start_screen(self):
        """
        Display text to pick difficulty alongside the different difficulty levels all in pre-made boxes
        """
        self._status.window_surface.blit(self._start_bg, (0, 0))
        # Draw title
        title_text = render_text(
            self.FONT_XLARGE, "Pick a difficulty", self._status.COLORS["WHITE"]
        )
        blit_text(self._status.window_surface, title_text, 90, 150)
        # Draw difficulty buttons
        draw_difficulty_buttons(
            self._status.window_surface,
            self._status.COLORS,
            self.FONT_DEFAULT,
        )
