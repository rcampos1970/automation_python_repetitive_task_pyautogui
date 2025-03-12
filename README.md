# Automated Repetitive Task with PyAutoGUI
## Overview
This project automates a repetitive, position-based task using Python's `pyautogui` library. The original task required consistent mouse movements and keyboard shortcuts, which I streamlined into an efficient script to save time and reduce manual errors.
## How It Works
The script performs a series of actions, including:
- Mouse clicks (single and double) at specific coordinates
- Keyboard shortcuts for copying, pasting, and confirming inputs
- Scrolling and navigation
It repeats the sequence 100 times, with pauses to account for loading times.
## Prerequisites
- Python 3.x
- PyAutoGUI (`pip install pyautogui`)
## Setup
1. Clone this repository.
   ```bash
   git clone <repo_url>
   cd <repo_folder>
   ```
2. Install the required package.
   ```bash
   pip install pyautogui
   ```
3. Adjust the coordinates (`x`, `y` values) in the script to match your screen and task setup. You can find coordinates using:
   ```python
   import pyautogui
   print(pyautogui.position())
   ```
## Usage
Run the script:
```bash
python automate_task.py
```
The script waits 7 seconds before starting, allowing you to switch to the correct window.
## Notes
- Ensure your screen resolution and application window match the expected layout for the script to work properly.
- You may need to fine-tune sleep durations or add error handling for more stability.

## Future Improvements
- Add error handling (e.g., detecting window focus or failures).
- Parameterize coordinates for easier customization.
- Implement logging for better tracking.

---
Happy automating!

