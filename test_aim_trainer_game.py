"""
Unit tests for aim trainer game
"""

import pytest
from aim_trainer_range import compute_accuracy


def test_compute_accuracy_half():
    """Test 50% accuracy"""
    assert compute_accuracy(1, 2) == 50


def test_compute_accuracy_third():
    """Test accuracy rounds correctly"""
    assert compute_accuracy(1, 3) == 33


def test_compute_accuracy_no_divide_by_zero():
    """Test that zero shots doesn't cause error"""
    result = compute_accuracy(5, 0)
    assert result == 0
