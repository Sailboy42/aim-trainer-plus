"""
Module for Aim Trainer
"""

import sys
import random
import pygame


def compute_accuracy(hits: int, shots: int) -> float:
    """
    Compute shooting accuracy as a percentage.

    Args:
        hits: Number of successful hits
        shots: Total number of shots taken

    Returns:
        Accuracy as a percentage (0-100), rounded to nearest integer
    """
    if shots != 0 and hits != 0:
        return round(hits / shots * 100)
    return 0


def get_difficulty_settings(difficulty: str) -> list:
    """
    Get game settings based on difficulty level.

    Args:
        difficulty: Difficulty level ("easy", "medium", "hard")

    Returns:
        list: [time_limit, num_targets, target_size]
    """
    settings = {
        "easy": [9, 2, 40],
        "medium": [6, 4, 30],
        "hard": [5, 5, 20],
    }
    return settings.get(difficulty, [])


def is_target_valid(target, min_x: int, min_y: int) -> bool:
    """
    Check if target spawned in valid area (not overlapping UI).

    Args:
        target: pygame.Rect object
        min_x: Minimum allowed x coordinate
        min_y: Minimum allowed y coordinate

    Returns:
        bool: True if target is valid
    """
    return target.topleft[0] >= min_x and target.topleft[1] >= min_y


def check_mouse_collision(mouse_x: int, mouse_y: int, target) -> bool:
    """
    Check if mouse position overlaps with target rectangle.

    Args:
        mouse_x: Mouse X coordinate
        mouse_y: Mouse Y coordinate
        target: pygame.Rect object

    Returns:
        bool: True if collision detected
    """
    return (
        mouse_x > target.topleft[0]
        and mouse_x < target.bottomright[0]
        and mouse_y > target.topleft[1]
        and mouse_y < target.bottomright[1]
    )


class AimTrainerRange:
    """
    aim trainer functions that handle data

    Attributes:
        COLORS: a dict with a string key indicating a color mapped to a tuple of ints representing a RGBa code
        WINDOW_HEIGHT: a int representing the amount of pixels wanted for height
        WINDOW_WIDTH: a int representing the amount of pixels wanted for width
        window_surface: a function that displays a window with given height and width
        main_clock: an object that helps track time
        _config: a list containing ints that determine game difficulty settings
        _tick_counter: a int of the time gone by in milliseconds
        _targets: a list containing cords for upcoming target spawn
        _amount_targets: a int indicating the amount of valid targets in play
        _score: a int indicating the score of the player
        FPS: a int indicating the FPS the game is being played at
        _hit_shots: a int indicating the amount of shots that hit a target
        _total_shots: a int indicating the amount of shots taken
        _MOUSE_Y: a int for the starting position of the mouse on y axis
        _MOUSE_X: a int for the starting position of the mouse on the x axis

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

    # Bounds for window
    window_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

    # time
    main_clock = pygame.time.Clock()

    def __init__(self):
        """
        Sets starting variables
        """
        # Game variables
        self._config = []
        self._tick_counter = 0
        self._targets = []
        self._amount_targets = 0
        self._score = 0
        self.fps = 75
        self._hit_shots = 0
        self._total_shots = 0
        # Mouse position
        self.mouse_y = round(self.WINDOW_HEIGHT / 2)
        self.mouse_x = round(self.WINDOW_WIDTH / 2)

    def config(self):
        """
        Returns:
            a list of ints being difficulty settings
        """
        return self._config

    def targets(self):
        """
        Returns:
            targets: a list of ints being future target spawn cords
        """
        return self._targets

    def score(self):
        """
        Returns:
            a int being the score
        """
        return self._score

    def terminate(self):
        """
        Ends Pygame
        """
        pygame.quit()
        sys.exit()

    def difficulty_boxes(self):
        """
        Generates box placement cords for difficulty text to be placed on

        Returns:
            a list of tuples containing ints which are cords/dim for boxes
        """
        difficulty_rects = []
        difficulty_rects.append(pygame.Rect(5, 450, 240, 100))
        difficulty_rects.append(pygame.Rect(255, 450, 240, 100))
        difficulty_rects.append(pygame.Rect(505, 450, 240, 100))
        return difficulty_rects

    def populate_config(self, difficulty):
        """
        Determine which settings will be used for game based off difficulty selected

        Args:
            difficulty: a string representing the difficulty

        Returns:
            a list containing ints that determine game difficulty settings
        """
        self._config = get_difficulty_settings(difficulty)
        return self._config

    def resize_target(self):
        """
        Resize target based off difficulty settings

        Returns:
            a image of the target
        """
        # Takes imported image
        target_image = pygame.image.load("target.png")
        # Scale image according to config
        target_image = pygame.transform.scale(
            target_image, (self._config[2], self._config[2])
        )
        return target_image

    def generate_targets(self):
        """
        Generate random placement of targets and add those cords to a list
        """
        self._targets.append(
            pygame.Rect(
                (random.randint(0, self.WINDOW_WIDTH - self._config[2])),
                (random.randint(0, self.WINDOW_HEIGHT - self._config[2])),
                self._config[2],
                self._config[2],
            )
        )

    def check_valid_target(self):
        """
        Check to see if target is in bound if is remove target from list and if not add to target counter
        """
        if not is_target_valid(self._targets[self._amount_targets], 135, 65):
            self._targets.pop(self._amount_targets)
        else:
            self._amount_targets += 1

    def check_target_hit(self):
        """
        Check to see if mouse position is the same as a target. If so remove target from screen, subtract from amount of visible targets, add to score, and add to hit count
        """
        # Check to see if mouse position overlaps with targets
        for target in self._targets[:]:
            # if target hit play hit sound, remove target, and add to score
            if check_mouse_collision(self.mouse_x, self.mouse_y, target):
                self._targets.remove(target)
                self._amount_targets -= 1
                self._score += 1
                self._hit_shots += 1
            self._total_shots += 1

    def time_actions(self):
        """
        Check time to see whether time is up or not. If times up, return False. If not subtract time from clock and return True

        Returns:
            a boolean determining if the game should continue or not
        """
        # Monitor if game is over my watching time
        if self._config[0] <= 0:
            # end game and display player stats
            return False
        self._tick_counter += 1

        if self._tick_counter % self.fps == 0:
            # game still going subtract from time
            self._config[0] -= 1
        return True

    def accuracy(self):
        """
        Calculates accuracy

        Returns:
            accuracy: a int being accuracy
        """
        return compute_accuracy(self._hit_shots, self._total_shots)
