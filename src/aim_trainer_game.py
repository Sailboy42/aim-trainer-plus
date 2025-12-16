"""
Orchestrates the aim trainer game loop.

Responsibilities:
- Initialize MVC components (Model: Range, View, Controller)
- Manage game states: difficulty selection, active gameplay, end screen
- Coordinate timing and event handling across components
"""

import pygame

from aim_trainer_range import AimTrainerRange
from aim_trainer_view import AimTrainerView
from aim_trainer_controller import AimTrainerController


def setup_game():
    """Initialize pygame and MVC components."""
    pygame.init()
    game_range = AimTrainerRange()
    view = AimTrainerView(game_range)
    controller = AimTrainerController(game_range)
    return game_range, view, controller


def run_difficulty_selection(game_range, view, controller):
    """Display difficulty selection screen and get user choice."""
    difficulty_selected = False
    while not difficulty_selected:
        controller.exit_program()
        view.start_screen()
        difficulty = controller.choose_difficulty()
        game_range.populate_config(difficulty)
        if game_range.config():
            difficulty_selected = True
        pygame.display.update()


def update_game_state(game_range, controller):
    """Update game state: targets, hits, time."""
    game_range.generate_targets()
    game_range.check_valid_target()
    controller.mouse_pos()
    game_range.check_target_hit()


def render_game_frame(view):
    """Render all game elements to screen."""
    view.game_background()
    view.game_status()
    view.display_targets()
    pygame.display.update()


def run_game_loop(game_range, view, controller):
    """Run active gameplay loop until time runs out."""
    game_active = True
    while game_active:
        controller.exit_program()
        update_game_state(game_range, controller)
        render_game_frame(view)
        game_active = game_range.time_actions()
    return game_active


def run_endgame_screen(view, controller):
    """Display endgame stats and handle restart/exit."""
    game_ended = False
    while not game_ended:
        controller.exit_program()
        view.endgame_screen()
        if controller.end_screen_check():
            main()
        pygame.display.update()


def main():
    """
    Main entry point for aim trainer.

    Game flow:
    1. Initialize components
    2. Difficulty selection
    3. Active gameplay
    4. Endgame screen
    """
    game_range, view, controller = setup_game()
    run_difficulty_selection(game_range, view, controller)
    run_game_loop(game_range, view, controller)
    run_endgame_screen(view, controller)


if __name__ == "__main__":
    main()
