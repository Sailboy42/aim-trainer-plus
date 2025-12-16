"""
Game logic and state management for aim trainer.

Responsibilities:
- Manage game configuration and difficulty settings
- Track game state: score, targets, time remaining
- Handle target generation, validation, and hit detection
- Calculate player accuracy and performance metrics
"""

import sys
import random

import pygame


class AimTrainerRange:
    """
    Model component managing game logic and state.

    Difficulty Settings:
    - Easy: 9 seconds, 2 targets, 40px size
    - Medium: 6 seconds, 4 targets, 30px size
    - Hard: 5 seconds, 5 targets, 20px size

    Attributes:
        COLORS: Color definitions (BLACK, WHITE, RED, BLUE)
        WINDOW_HEIGHT: Display height (768px)
        WINDOW_WIDTH: Display width (1366px)
        window_surface: Pygame display surface
        main_clock: Pygame clock for timing
        _config: Current difficulty settings [time, num_targets, target_size]
        _tick_counter: Frame counter for timing
        _targets: List of active target rectangles
        _amount_targets: Count of currently valid targets
        _score: Current player score
        FPS: Game frame rate (75)
        _hit_shots: Number of successful hits
        _total_shots: Total shots fired
        _MOUSE_X, _MOUSE_Y: Current mouse position
    """

    # Colors
    COLORS = {
        "BLACK": (0, 0, 0),
        "WHITE": (255, 255, 255),
        "RED": (255, 0, 0),
        "BLUE": (0, 0, 255),
    }

    # Window Size
    WINDOW_HEIGHT = 768
    WINDOW_WIDTH = 1366

    # Display and timing
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    main_clock = pygame.time.Clock()

    # Difficulty settings: (time_seconds, num_targets, target_size_px)
    DIFFICULTY_SETTINGS = {
        "easy": [9, 2, 40],
        "medium": [6, 4, 30],
        "hard": [5, 5, 20],
    }

    def __init__(self):
        """Initialize game state variables."""
        # Game configuration
        self._config = []

        # Timing
        self._tick_counter = 0
        self.FPS = 75

        # Target management
        self._targets = []
        self._amount_targets = 0

        # Scoring
        self._score = 0
        self._hit_shots = 0
        self._total_shots = 0

        # Input tracking
        self._MOUSE_X = round(self.WINDOW_WIDTH / 2)
        self._MOUSE_Y = round(self.WINDOW_HEIGHT / 2)

    # ==================== Configuration ====================

    def populate_config(self, difficulty):
        """
        Set game configuration based on selected difficulty.

        Args:
            difficulty: "easy", "medium", "hard", or None

        Returns:
            List of difficulty settings or empty list if invalid
        """
        if difficulty in self.DIFFICULTY_SETTINGS:
            self._config = self.DIFFICULTY_SETTINGS[difficulty].copy()
        else:
            self._config = []
        return self._config

    def get_difficulty_settings(self, difficulty):
        """
        Retrieve settings for a specific difficulty without applying them.

        Args:
            difficulty: Difficulty level as string

        Returns:
            List [time, num_targets, target_size] or None if invalid
        """
        return self.DIFFICULTY_SETTINGS.get(difficulty)

    def difficulty_boxes(self):
        """
        Generate selection boxes for difficulty buttons on start screen.

        Returns:
            List of pygame.Rect objects for easy, medium, and hard buttons
        """
        return [
            pygame.Rect(5, 450, 240, 100),  # Easy
            pygame.Rect(255, 450, 240, 100),  # Medium
            pygame.Rect(505, 450, 240, 100),  # Hard
        ]

    # ==================== Target Management ====================

    def generate_targets(self):
        """
        Spawn a new target at random position within valid bounds.

        Valid area excludes UI region in top-left (135x65px).
        """
        target_size = self._config[2]
        x = random.randint(0, self.WINDOW_WIDTH - target_size)
        y = random.randint(0, self.WINDOW_HEIGHT - target_size)
        self._targets.append(pygame.Rect(x, y, target_size, target_size))

    def is_target_valid(self, target):
        """
        Check if target is within valid play area.

        Args:
            target: pygame.Rect object representing target

        Returns:
            True if target doesn't overlap UI area, False otherwise
        """
        # UI region is top-left 135x65 pixels
        return not (target.topleft[0] < 135 and target.topleft[1] < 65)

    def check_valid_target(self):
        """
        Validate and remove out-of-bounds targets.

        Removes targets that overlap with UI area, increments counter
        for valid targets.
        """
        if self._amount_targets < len(self._targets):
            target = self._targets[self._amount_targets]
            if not self.is_target_valid(target):
                self._targets.pop(self._amount_targets)
            else:
                self._amount_targets += 1

    def resize_target(self):
        """
        Load and resize target image based on current difficulty.

        Returns:
            pygame.Surface scaled to current target size
        """
        target_image = pygame.image.load("target.png")
        size = self._config[2]
        return pygame.transform.scale(target_image, (size, size))

    # ==================== Hit Detection ====================

    def check_mouse_collision(self, mouse_x, mouse_y, target):
        """
        Check if mouse position overlaps with target rectangle.

        Args:
            mouse_x: Mouse x coordinate
            mouse_y: Mouse y coordinate
            target: pygame.Rect object

        Returns:
            True if collision detected, False otherwise
        """
        return (
            target.topleft[0] < mouse_x < target.bottomright[0]
            and target.topleft[1] < mouse_y < target.bottomright[1]
        )

    def check_target_hit(self):
        """
        Check for collisions between mouse and targets.

        For each hit:
        - Remove target from play
        - Increment score
        - Increment hit counter
        - Decrement active target count
        """
        for target in self._targets[:]:
            if self.check_mouse_collision(self._MOUSE_X, self._MOUSE_Y, target):
                self._targets.remove(target)
                self._amount_targets -= 1
                self._score += 1
                self._hit_shots += 1

    # ==================== Timing ====================

    def time_actions(self):
        """
        Update game timer and check if time has expired.

        Decrements remaining time once per second (at FPS rate).
        Returns:
            True if game should continue, False if time expired
        """
        if self._config[0] <= 0:
            return False

        self._tick_counter += 1
        if self._tick_counter % self.FPS == 0:
            self._config[0] -= 1

        return True

    # ==================== Scoring and Statistics ====================

    def accuracy(self):
        """
        Calculate player accuracy as percentage.

        Returns:
            Integer 0-100 representing hit percentage, 0 if no shots fired
        """
        if self._total_shots == 0:
            return 0
        return round(self._hit_shots / self._total_shots * 100)

    # ==================== Getters ====================

    def config(self):
        """Get current difficulty configuration."""
        return self._config

    def targets(self):
        """Get list of active targets."""
        return self._targets

    def score(self):
        """Get current score."""
        return self._score

    def MOUSE_X(self):
        """Get current mouse X position."""
        return self._MOUSE_X

    def MOUSE_Y(self):
        """Get current mouse Y position."""
        return self._MOUSE_Y

    # ==================== Utility ====================

    @staticmethod
    def terminate():
        """Clean shutdown of pygame and application."""
        pygame.quit()
        sys.exit()
