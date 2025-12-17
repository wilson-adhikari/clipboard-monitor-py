# Clipboard Monitor

A simple, cross-platform Python script that monitors your system clipboard for changes and prints new copied text in real-time.

Whenever you copy text (Ctrl+C / Cmd+C), it instantly detects and displays the content in the terminal. Includes a built-in function to simulate pasting (Ctrl+V / Cmd+V).

Perfect for debugging clipboard interactions, building automation tools, or extending into a full clipboard history manager.

## Features

- **Real-time clipboard monitoring** via efficient polling.
- **Cross-platform support**: Works on Windows, macOS, and Linux.
- Prints only new, non-empty text content.
- Graceful shutdown with Ctrl+C.
- Optional simulated paste functionality.
- Lightweight – no GUI, runs in the terminal.

## Requirements

- Python 3.6+
- `pyperclip` (for clipboard access)
- `pynput` (for simulating keyboard paste)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR-USERNAME/clipboard-monitor-py.git
   cd clipboard-monitor-py
