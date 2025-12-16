# Aim Trainer Plus

A pygame-based aim trainer to help improve mouse accuracy and speed through target practice exercises.

## Installation

Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the game:

```bash
python aim_trainer_game.py
```

## Testing

This project uses pytest for unit testing. Tests are located in `test_*.py` files and cover:

- Game logic and state management (`test_aim_trainer_range.py`)
- Input handling and user interactions (`test_aim_trainer_controller.py`)
- Rendering and UI components (`test_aim_trainer_view.py`)

### Running Tests

Run all tests:

```bash
pytest
```

Run with verbose output:

```bash
pytest -v
```

Run specific test file:

```bash
pytest test_aim_trainer_range.py
```

Run tests with coverage report:

```bash
pytest --cov=. --cov-report=html
```

### Test Coverage

The test suite includes:
- Initialization and configuration tests
- Difficulty setting validation
- Target generation and hit detection
- Score and accuracy calculations
- Game state transitions
- UI component functionality

