#!/usr/bin/env python3
"""
Main entry point for Aim Trainer Plus.

Run this file to start the game:
    python main.py
"""

import sys
from pathlib import Path

# Add src directory to path for imports
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

from aim_trainer_game import main

if __name__ == "__main__":
    main()
