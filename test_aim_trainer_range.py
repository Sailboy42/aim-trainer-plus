"""
Unit tests for aim trainer range
"""

import pytest
from aim_trainer_range import compute_accuracy, AimTrainerRange


def test_compute_accuracy_basic():
    """Test basic accuracy calculation"""
    assert compute_accuracy(5, 10) == 50


def test_compute_accuracy_perfect():
    """Test 100% accuracy"""
    assert compute_accuracy(10, 10) == 100


def test_compute_accuracy_zero_shots():
    """Test accuracy when no shots taken"""
    assert compute_accuracy(0, 0) == 0


def test_compute_accuracy_zero_hits():
    """Test accuracy when no hits"""
    assert compute_accuracy(0, 10) == 0


def test_difficulty_boxes_amount():
    """Check that correct amount of boxes are added to list"""
    game_range = AimTrainerRange()
    assert len(game_range.difficulty_boxes()) == 3


def test_populate_config_easy():
    """Check that populate config returns proper list settings for easy difficulty"""
    game_range = AimTrainerRange()
    result = game_range.populate_config("easy")
    assert len(result) == 3
    assert result[2] == 40  # target size for easy mode


def test_populate_config_medium():
    """Check that populate config returns proper list settings for medium difficulty"""
    game_range = AimTrainerRange()
    result = game_range.populate_config("medium")
    assert len(result) == 3
    assert result[2] == 30  # target size for medium mode


def test_populate_config_hard():
    """Check that populate config returns proper list settings for hard difficulty"""
    game_range = AimTrainerRange()
    result = game_range.populate_config("hard")
    assert len(result) == 3
    assert result[2] == 20  # target size for hard mode


def test_range_initialization():
    """Test that AimTrainerRange initializes with correct default values"""
    game_range = AimTrainerRange()
    assert game_range.score() == 0
    assert game_range._hit_shots == 0
    assert game_range._total_shots == 0
    assert game_range.config() == []
    assert game_range.targets() == []


def test_target_hit_detection():
    """Test that target hit detection works correctly"""
    game_range = AimTrainerRange()
    game_range.populate_config("easy")

    # Add a target manually at a known position
    import pygame

    pygame.init()
    target_rect = pygame.Rect(100, 100, 40, 40)
    game_range._targets.append(target_rect)

    # Set mouse position inside target
    game_range.mouse_x = 120
    game_range.mouse_y = 120

    initial_score = game_range.score()
    game_range.check_target_hit()

    # Check that target was hit and removed
    assert game_range.score() == initial_score + 1
    assert game_range._hit_shots == 1
    assert len(game_range.targets()) == 0


def test_target_miss_detection():
    """Test that missed shots are counted correctly"""
    game_range = AimTrainerRange()
    game_range.populate_config("easy")

    # Add a target manually at a known position
    import pygame

    pygame.init()
    target_rect = pygame.Rect(100, 100, 40, 40)
    game_range._targets.append(target_rect)

    # Set mouse position outside target
    game_range._MOUSE_X = 200
    game_range._MOUSE_Y = 200

    initial_score = game_range.score()
    game_range.check_target_hit()

    # Check that score didn't increase but shot was counted
    assert game_range.score() == initial_score
    assert len(game_range.targets()) == 1  # target still there


def test_game_end_condition_time_up():
    """Test that game ends when time runs out"""
    game_range = AimTrainerRange()
    game_range.populate_config("easy")

    # Set time to 0
    game_range._config[0] = 0

    # time_actions should return False when time is up
    assert game_range.time_actions() is False


def test_game_continues_with_time():
    """Test that game continues when time remains"""
    game_range = AimTrainerRange()
    game_range.populate_config("easy")

    # Ensure time is above 0
    game_range._config[0] = 5

    # time_actions should return True when time remains
    assert game_range.time_actions() is True
