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


# Edge case tests
def test_view_status_attribute(view_with_range):
    """Test that view maintains status attribute"""
    view, game_range = view_with_range
    assert hasattr(view, '_status')
    assert view._status is game_range


def test_view_font_initialization(view_with_range):
    """Test that view initializes font correctly"""
    view, game_range = view_with_range
    assert view.FONT is not None
    assert isinstance(view.FONT, pygame.font.Font)


def test_view_backgrounds_loaded(view_with_range):
    """Test that view loads background images"""
    view, game_range = view_with_range
    assert hasattr(view, '_start_bg')
    assert hasattr(view, '_end_bg')
    assert hasattr(view, '_range_bg')


def test_backgrounds_are_surfaces(view_with_range):
    """Test that backgrounds are pygame surfaces"""
    view, game_range = view_with_range
    assert isinstance(view._start_bg, pygame.Surface)
    assert isinstance(view._end_bg, pygame.Surface)
    assert isinstance(view._range_bg, pygame.Surface)


def test_draw_text_empty_string(view_with_range):
    """Test draw_text with empty string"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    # Should handle empty strings gracefully
    view.draw_text("", surface, 10, 10)


def test_draw_text_long_string(view_with_range):
    """Test draw_text with very long string"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    long_text = "A" * 1000
    # Should handle long strings
    view.draw_text(long_text, surface, 10, 10)


def test_draw_text_special_characters(view_with_range):
    """Test draw_text with special characters"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    special_text = "!@#$%^&*()_+-=[]{}|;':\",./<>?"
    # Should handle special characters
    view.draw_text(special_text, surface, 10, 10)


def test_draw_text_unicode_characters(view_with_range):
    """Test draw_text with unicode characters"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    unicode_text = "你好世界 مرحبا العالم"
    # Should handle unicode (if font supports it)
    view.draw_text(unicode_text, surface, 10, 10)


def test_draw_text_edge_coordinates(view_with_range):
    """Test draw_text at screen edges"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    
    # Test corners
    corners = [(0, 0), (800, 600), (0, 600), (800, 0)]
    for x, y in corners:
        view.draw_text("Test", surface, x, y)


def test_draw_text_negative_coordinates(view_with_range):
    """Test draw_text with negative coordinates (off-screen)"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    # Should handle negative coordinates without crashing
    view.draw_text("Test", surface, -100, -100)


def test_draw_text_large_coordinates(view_with_range):
    """Test draw_text with coordinates beyond surface"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    # Should handle coordinates beyond surface bounds
    view.draw_text("Test", surface, 10000, 10000)


def test_multiple_text_draws_same_surface(view_with_range):
    """Test drawing multiple texts on same surface"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    
    texts = ["Text 1", "Text 2", "Text 3", "Text 4"]
    for i, text in enumerate(texts):
        view.draw_text(text, surface, i * 100, i * 100)


def test_draw_text_with_custom_font(view_with_range):
    """Test draw_text with custom font parameter"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    custom_font = pygame.font.SysFont('arial', 24)
    view.draw_text("Test", surface, 10, 10, font=custom_font)


def test_draw_text_with_custom_color(view_with_range):
    """Test draw_text with custom color parameter"""
    view, game_range = view_with_range
    surface = pygame.Surface((800, 600))
    custom_color = (255, 0, 0)  # Red
    view.draw_text("Test", surface, 10, 10, color=custom_color)


