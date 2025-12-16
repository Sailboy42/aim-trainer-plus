# Aim Trainer Plus

A pygame-based aim trainer to improve mouse accuracy and speed through target practice exercises. Features progressive difficulty levels (Easy, Medium, Hard) with real-time score tracking and accuracy metrics.

## Architecture

This project uses the **Model-View-Controller (MVC)** pattern:

- **Model** (`aim_trainer_range.py`): Game logic, state management, scoring
- **View** (`aim_trainer_view.py`): UI rendering, backgrounds, text, targets
- **Controller** (`aim_trainer_controller.py`): Input handling, event processing
- **Orchestrator** (`aim_trainer_game.py`): Game loop and state coordination

### Component Responsibilities

#### Model (AimTrainerRange)
- Manage difficulty configurations and game settings
- Generate and validate targets
- Detect mouse-target collisions
- Track score, accuracy, and game time
- Coordinate game state transitions

#### View (AimTrainerView)
- Render difficulty selection screen
- Display gameplay with targets and HUD
- Show endgame statistics
- Handle all text and image rendering

#### Controller (AimTrainerController)
- Capture mouse clicks and motion
- Detect difficulty button selections
- Monitor exit signals (ESC key, window close)
- Update model with user input

#### Orchestrator (aim_trainer_game.py)
- Initialize MVC components
- Manage game flow: selection → gameplay → endscreen
- Coordinate component interactions

## Difficulty Levels

| Difficulty | Time (s) | Targets | Size (px) |
|------------|---------|---------|-----------|
| Easy       | 9       | 2       | 40×40     |
| Medium     | 6       | 4       | 30×30     |
| Hard       | 5       | 5       | 20×20     |

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

**Gameplay:**
1. Select difficulty from the start screen (Easy/Medium/Hard)
2. Click targets as they appear within the time limit
3. View final score and accuracy on the endgame screen
4. Click to restart

**Controls:**
- Mouse click: Select difficulty, click targets
- ESC or close window: Exit game

## Testing

This project uses pytest for comprehensive unit testing. Tests cover game logic, input handling, and UI components across three test modules.

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
pytest test_aim_trainer_range.py -v
```

Run tests with coverage report:

```bash
pytest --cov=. --cov-report=html
```

### Test Coverage

**Game Logic Tests** (`test_aim_trainer_range.py` - 27 tests):
- Configuration and difficulty settings
- Target generation and validation
- Hit detection and collision physics
- Accuracy and score calculations
- Time management and game timing
- Edge cases: zero shots, boundary clicks, invalid difficulties

**Input Tests** (`test_aim_trainer_controller.py` - 10 tests):
- Difficulty selection detection
- Mouse position tracking
- Exit signal handling (ESC, window close)
- Event validation

**Rendering Tests** (`test_aim_trainer_view.py` - 16 tests):
- Font and background initialization
- Text rendering with edge cases
- Coordinate handling (corners, negative, beyond bounds)
- Custom font and color parameters

**Total: 53 tests, all passing (0.29s execution)**

## Project Structure

```
aim-trainer-plus/
├── aim_trainer_game.py      # Game orchestrator
├── aim_trainer_range.py     # Model (game logic)
├── aim_trainer_controller.py # Controller (input)
├── aim_trainer_view.py      # View (rendering)
├── test_aim_trainer_*.py    # Test suite (53 tests)
├── requirements.txt         # Python dependencies
├── README.md               # This file
└── assets/                 # Images and fonts
    ├── range-start.png     # Start screen background
    ├── range2.png          # Gameplay background
    ├── range-end.png       # Endgame screen background
    ├── target.png          # Target image
    └── cs_regular.ttf      # Font file
```
