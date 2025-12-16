"""
Unit tests for aim_trainer_controller.py
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

import pytest
import pygame
from aim_trainer_controller import AimTrainerController
from aim_trainer_range import AimTrainerRange


@pytest.fixture
def controller_with_range():
    """Fixture to create controller with range instance"""
    pygame.init()
    game_range = AimTrainerRange()
    controller = AimTrainerController(game_range)
    return controller, game_range


def test_controller_initialization(controller_with_range):
    """Test that controller initializes with status"""
    controller, game_range = controller_with_range
    assert controller._status == game_range


def test_choose_difficulty_returns_none_without_click():
    """Test choose_difficulty returns None when no click event"""
    pygame.init()
    game_range = AimTrainerRange()
    controller = AimTrainerController(game_range)

    # Clear event queue
    pygame.event.clear()
    result = controller.choose_difficulty()
    assert result is None


# Edge case tests
def test_controller_status_attribute(controller_with_range):
    """Test that controller maintains status attribute"""
    controller, game_range = controller_with_range
    assert hasattr(controller, "_status")
    assert controller._status is game_range


def test_controller_with_none_range():
    """Test controller behavior when initialized with None status"""
    pygame.init()
    # This tests that controller can be created without a range
    # (edge case - normally not done but testing robustness)
    controller = AimTrainerController(None)
    assert controller._status is None


def test_choose_difficulty_all_three_options(controller_with_range):
    """Test that all three difficulty options are available"""
    controller, game_range = controller_with_range
    boxes = game_range.difficulty_boxes()
    assert len(boxes) == 3


def test_mouse_pos_method_exists(controller_with_range):
    """Test that mouse_pos method exists and can be called"""
    controller, game_range = controller_with_range
    assert hasattr(controller, "mouse_pos")
    assert callable(controller.mouse_pos)


def test_exit_program_method_exists(controller_with_range):
    """Test that exit_program method exists"""
    controller, game_range = controller_with_range
    assert hasattr(controller, "exit_program")
    assert callable(controller.exit_program)


def test_end_screen_check_method_exists(controller_with_range):
    """Test that end_screen_check method exists"""
    controller, game_range = controller_with_range
    assert hasattr(controller, "end_screen_check")
    assert callable(controller.end_screen_check)


def test_choose_difficulty_returns_string_or_none(controller_with_range):
    """Test that choose_difficulty returns either a string or None"""
    controller, game_range = controller_with_range
    pygame.event.clear()
    result = controller.choose_difficulty()
    assert result is None or isinstance(result, str)


def test_choose_difficulty_valid_difficulties(controller_with_range):
    """Test that choose_difficulty only returns valid difficulty strings"""
    controller, game_range = controller_with_range
    pygame.event.clear()
    result = controller.choose_difficulty()
    valid_difficulties = [None, "easy", "medium", "hard"]
    assert result in valid_difficulties
