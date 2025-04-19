## Author

© 2025 Vladut Ene | enevlad28@gmail.com

## log_monitoring_app
This is a Repository created for a Log Monitoring application written in Python.

This Python script parses a `logs.log` file and calculates the runtime duration of jobs based on their `START` and `END` timestamps. It flags any job that exceeds a defined threshold with a `WARNING` or `ERROR` level, outputing them in the CLI and a separate TXT file.
More details can be found in: [Log Monitoring Application 1.pdf]
  *if there is a delay in generating the outputs, it can be because the flush() is not used; It can be added as feature but only if the buffer needs this feature.

## Requirements
Python 3.7 or higher

## 🔧 Installing Python (if not already installed)
_Windows:_
Download the installer from python.org/downloads. Run the installer and make sure to check "Add Python to PATH".
Verify installation:   _#python --version_

_macOS:_
Install Homebrew (if not installed): _/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)_
Install Python: _brew install python_
Verify: _python3 --version_

_Linux (Debian/Ubuntu):_ 
Install Python: _sudo apt update; sudo apt install python3 python3-pip;_

## How to run the Script
1. Clone the repository or download the source files.
2. Open a terminal (e.g. VSCode) and navigate to the project directory.
3. Make sure the _logs.log_ file is present in the same directory.
4. Run the script: _python log_monitor_alert.py_

