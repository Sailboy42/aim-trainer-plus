"""
Unit tests for aim_trainer_controller.py
"""
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
