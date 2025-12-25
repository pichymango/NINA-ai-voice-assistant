import subprocess
import re

def set_volume(percent: int) -> str:
    percent = max(0, min(100, percent))  # clamp 0–100

    subprocess.run([
        "osascript", "-e",
        f"set volume output volume {percent}"
    ])

    return f"Volume set to {percent} percent"


def mute() -> str:
    subprocess.run([
        "osascript", "-e",
        "set volume with output muted"
    ])
    return "Muted"
