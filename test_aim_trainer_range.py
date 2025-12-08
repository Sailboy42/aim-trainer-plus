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
