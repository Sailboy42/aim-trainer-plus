"""
Unit tests for aim_trainer_range.py
"""

import pytest
import pygame
from aim_trainer_range import AimTrainerRange


@pytest.fixture
def game_range():
    """Fixture to create a fresh AimTrainerRange instance for each test"""
    pygame.init()
    return AimTrainerRange()


def test_range_initialization(game_range):
    """Test that AimTrainerRange initializes with correct default values"""
    assert game_range._config == []
    assert game_range._tick_counter == 0
    assert game_range._targets == []
    assert game_range._amount_targets == 0
    assert game_range._score == 0
    assert game_range.FPS == 75
    assert game_range._MOUSE_Y == round(game_range.WINDOW_HEIGHT / 2)
    assert game_range._MOUSE_X == round(game_range.WINDOW_WIDTH / 2)


def test_difficulty_boxes_amount(game_range):
    """Test that difficulty_boxes returns 3 rectangles"""
    boxes = game_range.difficulty_boxes()
    assert len(boxes) == 3
    assert all(isinstance(box, pygame.Rect) for box in boxes)


def test_populate_config_easy(game_range):
    """Test populate_config with easy difficulty"""
    config = game_range.populate_config("easy")
    assert config == [9, 2, 40]
    assert game_range._config == [9, 2, 40]


def test_populate_config_medium(game_range):
    """Test populate_config with medium difficulty"""
    config = game_range.populate_config("medium")
    assert config == [6, 4, 30]
    assert game_range._config == [6, 4, 30]


def test_populate_config_hard(game_range):
    """Test populate_config with hard difficulty"""
    config = game_range.populate_config("hard")
    assert config == [5, 5, 20]
    assert game_range._config == [5, 5, 20]


def test_config_getter(game_range):
    """Test that config() returns the internal config"""
    game_range.populate_config("easy")
    assert game_range.config() == [9, 2, 40]


def test_score_getter(game_range):
    """Test that score() returns the current score"""
    assert game_range.score() == 0
    game_range._score = 10
    assert game_range.score() == 10


def test_targets_getter(game_range):
    """Test that targets() returns the targets list"""
    assert game_range.targets() == []
    game_range._targets.append(pygame.Rect(0, 0, 10, 10))
    assert len(game_range.targets()) == 1


def test_generate_targets(game_range):
    """Test that generate_targets adds a target"""
    game_range.populate_config("easy")
    initial_count = len(game_range._targets)
    game_range.generate_targets()
    assert len(game_range._targets) == initial_count + 1


def test_time_actions_time_up(game_range):
    """Test time_actions when time is up"""
    game_range.populate_config("easy")
    game_range._config[0] = 0
    result = game_range.time_actions()
    assert result is False


def test_time_actions_time_remaining(game_range):
    """Test time_actions when time is remaining"""
    game_range.populate_config("easy")
    result = game_range.time_actions()
    assert result is True


def test_accuracy_calculation(game_range):
    """Test accuracy calculation"""
    game_range._hitShots = 7
    game_range._totalShots = 10
    accuracy = game_range.accuracy()
    assert accuracy == 70


def test_accuracy_zero_shots(game_range):
    """Test accuracy when no shots taken"""
    game_range._hitShots = 0
    game_range._totalShots = 0
    accuracy = game_range.accuracy()
    assert accuracy == 0


def test_check_valid_target_invalid_position(game_range):
    """Test check_valid_target removes targets in invalid position"""
    game_range.populate_config("easy")
    game_range._targets.append(pygame.Rect(50, 30, 40, 40))
    game_range._amount_targets = 0
    game_range.check_valid_target()
    assert len(game_range._targets) == 0


def test_check_valid_target_valid_position(game_range):
    """Test check_valid_target keeps targets in valid position"""
    game_range.populate_config("easy")
    game_range._targets.append(pygame.Rect(200, 200, 40, 40))
    game_range._amount_targets = 0
    game_range.check_valid_target()
    assert len(game_range._targets) == 1
    assert game_range._amount_targets == 1


def test_resize_target(game_range):
    """Test that resize_target returns correctly sized image"""
    game_range.populate_config("easy")
    target_image = game_range.resize_target()
    assert target_image.get_width() == 40
    assert target_image.get_height() == 40
