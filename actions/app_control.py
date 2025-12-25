import subprocess


def open_app(app_name: str) -> str:
    try:
        subprocess.run(
            ["open", "-a", app_name],
            check=True
        )
        return f"Opening {app_name}"
    except subprocess.CalledProcessError:
        return f"I couldn't find {app_name}"


def close_app(app_name: str) -> str:
    try:
        subprocess.run(
            ["osascript", "-e", f'tell application "{app_name}" to quit'],
            check=True
        )
        return f"Closed {app_name}"
    except subprocess.CalledProcessError:
        return f"I couldn't close {app_name}"
