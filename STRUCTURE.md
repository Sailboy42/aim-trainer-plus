# Project Organization

This document describes the optimal file organization implemented for Aim Trainer Plus.

## Directory Structure

```
aim-trainer-plus/
├── main.py                 # Entry point - run this to start the game
├── setup.py                # Package distribution configuration
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Project metadata and tool configuration
├── README.md              # User documentation
├── .gitignore             # Git exclusions
│
├── src/                    # Source code (MVC components)
│   ├── __init__.py
│   ├── aim_trainer_game.py      # Orchestrator - game loop coordination
│   ├── aim_trainer_range.py     # Model - game logic and state
│   ├── aim_trainer_controller.py # Controller - input handling
│   └── aim_trainer_view.py      # View - rendering and UI
│
├── tests/                  # Test suite (53 tests)
│   ├── __init__.py
│   ├── test_aim_trainer_range.py
│   ├── test_aim_trainer_controller.py
│   └── test_aim_trainer_view.py
│
└── assets/                 # Game assets
    ├── *.png              # Background and sprite images
    ├── *.ttf              # Font files
    └── *.wav              # Sound effects
```

## Benefits of This Organization

### 1. **Clear Separation of Concerns**
   - Source code in `src/`
   - Tests in `tests/`
   - Assets in `assets/`
   - Configuration at root

### 2. **Scalability**
   - Easy to add new modules to `src/`
   - Tests mirror source structure
   - Assets organized by type

### 3. **Import Clarity**
   - All source imports from `src/` package
   - Tests use explicit path setup
   - No ambiguous module resolution

### 4. **Professional Standards**
   - Follows Python packaging conventions
   - Compatible with pip installation
   - Ready for distribution (setup.py)

### 5. **Development Workflow**
   - Run game: `python main.py`
   - Run tests: `pytest tests/`
   - Install package: `pip install -e .`

## Key Files

- **main.py**: Single entry point for end users
- **setup.py**: Enables `pip install` and package distribution
- **pyproject.toml**: Modern Python project configuration
- **src/__init__.py**: Package initialization with version info
- **tests/__init__.py**: Test suite initialization

## Asset Management

All assets use relative paths from `src/` directory:
```python
assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
```

This ensures assets load correctly regardless of:
- Current working directory
- Installation method (dev vs pip install)
- Execution context (script vs module)
