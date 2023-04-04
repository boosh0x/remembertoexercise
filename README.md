# Reminder to Exercise

## Overview

Reminder to Exercise is a simple and effective Python application designed to remind you to take breaks, stretch, and do some physical activity every hour. The app features a countdown timer and plays a fun and motivational audio clip to keep you engaged and motivated throughout the day. By encouraging regular physical activity, Reminder to Exercise aims to improve your overall health and productivity.

## Features

- Customizable countdown timer: Set the timer to your desired interval (default is one hour).
- Fun and motivational audio reminders: Add your own audio clips to keep things interesting and motivating.
- Start, pause, reset, and quit options: Easily control the application with intuitive buttons.
- Lightweight and cross-platform: Works on macOS, with the potential to be adapted for other platforms.

## Installation

1. Install Python 3.x on your system.
2. Install the required packages using pip:

```bash

pip install playsound PyObjC
```

3. Clone this repository or download the source code.

```bash

git clone https://github.com/yourusername/reminder-to-exercise.git
```

4. Replace the placeholder audio file path in the code with the path to your custom audio clip or use the sample audio included:

```python

playsound("path/to/your/audio/file.mp3")
```

## Usage

1. Open a terminal and navigate to the folder containing the reminder_to_exercise.py file.
    Run the application using the following command:

```bash

python3 reminder_to_exercise.py
```

2. Use the "Start", "Pause", "Reset", and "Quit" buttons to control the timer and application.

## Contributing

We welcome contributions to improve Reminder to Exercise. If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch with a descriptive name, such as feature-add-new-button or bugfix-timer-issue.
3. Make your changes and commit them with clear and concise commit messages.
4. Submit a pull request with a detailed description of your changes.

## License

This project is released under the MIT License. See LICENSE for more information.
