import subprocess

def take_screenshot():
    subprocess.run(["screencapture", "-x", "screenshot.png"])
    return "Screenshot taken"

def lock_screen():
    subprocess.run([
        "osascript",
        "-e",
        'tell application "System Events" to keystroke "q" using {control down, command down}'
    ])
    return "Screen locked"


def show_desktop():
    subprocess.run([
        "osascript", "-e",
        'tell application "System Events" to key code 103'
    ])
    return "Showing desktop"

def minimize_window():
    subprocess.run([
        "osascript", "-e",
        'tell application "System Events" to keystroke "m" using command down'
    ])
    return "Window minimized"

def switch_app(app_name: str):
    subprocess.run([
        "osascript", "-e",
        f'tell application "{app_name}" to activate'
    ])
    return f"Switching to {app_name}"
