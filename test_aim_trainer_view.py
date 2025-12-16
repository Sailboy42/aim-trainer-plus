"""
Unit tests for aim_trainer_view.py
"""
import pytest
import pygame
from aim_trainer_view import AimTrainerView
from aim_trainer_range import AimTrainerRange


@pytest.fixture
def view_with_range():
    """Fixture to create view with range instance"""
    pygame.init()
    game_range = AimTrainerRange()
    view = AimTrainerView(game_range)
    return view, game_range


def test_view_initialization(view_with_range):
    """Test that view initializes correctly"""
    view, game_range = view_with_range
    assert view._status == game_range
    assert view.FONT is not None


def test_draw_text_with_defaults(view_with_range):
    """Test draw_text uses default font and color"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    # Should not raise exception
    view.draw_text("Test", surface, 10, 10)
