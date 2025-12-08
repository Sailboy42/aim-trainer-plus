"""
Compiles aim trainer mvc files.
"""
import pygame

from aim_trainer_range import AimTrainerRange
from aim_trainer_view import AimTrainerView
from aim_trainer_controller import AimTrainerController


def main():
    """
    Runs aim trainer
    """
    pygame.init()

    game_range = AimTrainerRange()
    view = AimTrainerView(game_range)
    controller = AimTrainerController(game_range)

    # Start screen
    start = False
    while not start:
        controller.exit_program()
        view.start_screen()
        game_range.populate_config(controller.choose_difficulty())
        if game_range.config():
            start = True
        pygame.display.update()

    # game
    while start:
        controller.exit_program()
        view.game_background()
        view.game_status()
        game_range.generate_targets()
        game_range.check_valid_target()
        view.display_targets()
        controller.mouse_pos()
        game_range.check_target_hit()
        start = game_range.time_actions()
        pygame.display.update()

        # end screen
        while not start:
            controller.exit_program()
            view.endgame_screen()
            if controller.end_screen_check():
                main()
                return
            pygame.display.update()


if __name__ == "__main__":
    main()
