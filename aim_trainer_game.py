"""
Compiles aim trainer mvc files.
"""

import pygame

from aim_trainer_range import AimTrainerRange
from aim_trainer_view import AimTrainerView
from aim_trainer_controller import AimTrainerController


def setup_game():
    """
    Initialize pygame and create MVC components.

    Returns:
        tuple: (game_range, view, controller) instances
    """
    pygame.init()
    game_range = AimTrainerRange()
    view = AimTrainerView(game_range)
    controller = AimTrainerController(game_range)
    return game_range, view, controller


def run_difficulty_selection(game_range, view, controller):
    """
    Display difficulty selection screen and wait for user choice.

    Args:
        game_range: AimTrainerRange instance
        view: AimTrainerView instance
        controller: AimTrainerController instance

    Returns:
        bool: True when difficulty is selected
    """
    while True:
        controller.exit_program()
        view.start_screen()
        game_range.populate_config(controller.choose_difficulty())
        if game_range.config():
            return True
        pygame.display.update()


def update_game_state(game_range, view, controller):
    """
    Update game state for one frame during gameplay.

    Args:
        game_range: AimTrainerRange instance
        view: AimTrainerView instance
        controller: AimTrainerController instance

    Returns:
        bool: False if game time is up, True otherwise
    """
    controller.exit_program()
    view.game_background()
    view.game_status()
    game_range.generate_targets()
    game_range.check_valid_target()
    view.display_targets()
    controller.mouse_pos()
    game_range.check_target_hit()
    game_continues = game_range.time_actions()
    pygame.display.update()
    return game_continues


def run_game_loop(game_range, view, controller):
    """
    Main gameplay loop.

    Args:
        game_range: AimTrainerRange instance
        view: AimTrainerView instance
        controller: AimTrainerController instance
    """
    while True:
        game_continues = update_game_state(game_range, view, controller)
        if not game_continues:
            run_endgame_screen(view, controller)
            break


def run_endgame_screen(view, controller):
    """
    Display endgame screen and handle restart logic.

    Args:
        view: AimTrainerView instance
        controller: AimTrainerController instance
    """
    while True:
        controller.exit_program()
        view.endgame_screen()
        if controller.end_screen_check():
            main()
            return
        pygame.display.update()


def main():
    """
    Main entry point for the aim trainer game.
    """
    game_range, view, controller = setup_game()
    run_difficulty_selection(game_range, view, controller)
    run_game_loop(game_range, view, controller)


if __name__ == "__main__":
    main()
