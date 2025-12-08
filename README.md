# Aim Trainer Plus

A pygame-based aim trainer to practice mouse accuracy and speed.

**Original Project:** Part of Software Design (SoftDes) course group project.

## Project Structure

```
aim-trainer-plus/
├── aim_trainer_game.py       # Main game orchestration
├── aim_trainer_range.py      # Game logic and state management
├── aim_trainer_controller.py # Input handling
├── aim_trainer_view.py       # Rendering and UI
├── test_aim_trainer_*.py     # Unit tests
├── requirements.txt          # Python dependencies
├── target.png                # Target sprite image
├── range-start.png           # Start screen background
├── range-end.png             # End screen background
├── range2.png                # Gameplay background
├── cs_regular.ttf            # Custom font
└── README.md                 # This file
```

## Requirements

To install required packages and libraries:

```bash
pip install -r requirements.txt
```

## How to Play

1. Run `python aim_trainer_game.py`
2. Select difficulty (easy, medium, or hard)
3. Click on targets as they appear
4. Try to achieve the highest score and accuracy
5. Exit or Escape out at any time

## Difficulty Levels

- **Easy**: 9 seconds, 2 targets, 40x40 px
- **Medium**: 6 seconds, 4 targets, 30x30 px
- **Hard**: 5 seconds, 5 targets, 20x20 px

## Running Tests

Install dependencies, then run:

```bash
pytest
```

For verbose output:

```bash
pytest -v
```

To check code quality:

```bash
pylint aim_trainer_*.py
```

## Architecture

The project follows the **Model-View-Controller (MVC)** pattern:

- **Model** (`aim_trainer_range.py`): Game state, target management, hit detection, difficulty settings
- **View** (`aim_trainer_view.py`): Rendering sprites, backgrounds, UI text, game stats
- **Controller** (`aim_trainer_controller.py`): Input handling (mouse, keyboard, difficulty selection)
- **Main** (`aim_trainer_game.py`): Game loop orchestration and state transitions
