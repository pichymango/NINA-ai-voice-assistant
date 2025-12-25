import subprocess

def play_pause() -> str:
    subprocess.run([
        "osascript",
        "-e",
        'tell application "System Events" to key code 49'
    ])
    return "Toggling play pause"

def next_track() -> str:
    subprocess.run([
        "osascript",
        "-e",
        'tell application "System Events" to key code 124 using command down'
    ])
    return "Skipping to next"

def previous_track() -> str:
    subprocess.run([
        "osascript",
        "-e",
        'tell application "System Events" to key code 123 using command down'
    ])
    return "Going to previous"
