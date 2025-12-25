from dotenv import load_dotenv
load_dotenv()

from speech import speak, listen
from ai.gemini_brain import think

import random

from actions.app_control import open_app, close_app
from actions.browser_control import open_website, play_youtube, search_web
from actions.maps_control import open_location
from actions.weather_control import get_weather
from actions.system_automation import (
    take_screenshot,
    lock_screen,
    show_desktop,
    minimize_window,
    switch_app
)


def maybe_acknowledge():
    if random.random() < 0.4:
        speak("On it Boss")


def nina_loop():
    speak("Nina online. I'm listening Boss.")
    print("Nina online. Listening...")

    while True:
        user_input = listen()
        if not user_input:
            continue

        text = user_input.lower().strip()

        if text in ("exit", "quit", "shutdown"):
            speak("Shutting down Boss.")
            break

        if "screenshot" in text:
            maybe_acknowledge()
            speak(take_screenshot())
            continue

        if "lock screen" in text:
            maybe_acknowledge()
            speak(lock_screen())
            continue

        if "show desktop" in text:
            maybe_acknowledge()
            speak(show_desktop())
            continue

        if "minimize" in text:
            maybe_acknowledge()
            speak(minimize_window())
            continue

        if text.startswith("switch to "):
            maybe_acknowledge()
            app = text.replace("switch to", "").strip().title()
            speak(switch_app(app))
            continue

        if text.startswith("search "):
            maybe_acknowledge()
            speak(search_web(text.replace("search", "", 1).strip()))
            continue

        if "maps" in text:
            maybe_acknowledge()
            location = (
                text.replace("on maps", "")
                .replace("maps", "")
                .replace("find", "")
                .replace("search", "")
                .strip()
            )
            speak(open_location(location))
            continue

        if "weather" in text:
            city = (
                text.replace("weather", "")
                .replace("in", "")
                .replace("at", "")
                .replace("of", "")
                .strip()
            )
            speak(get_weather(city))
            continue

        if "play" in text and "youtube" in text:
            maybe_acknowledge()
            query = (
                text.replace("play", "")
                .replace("on youtube", "")
                .replace("youtube", "")
                .strip()
            )
            speak(play_youtube(query))
            continue

        if text.startswith("close "):
            maybe_acknowledge()
            app = text.replace("close", "", 1).strip().title()
            speak(close_app(app))
            continue

        if text.startswith("open ") and "." in text:
            maybe_acknowledge()
            speak(open_website(text.replace("open", "", 1).strip()))
            continue

        if text.startswith("open "):
            maybe_acknowledge()
            app = text.replace("open", "", 1).strip().title()
            speak(open_app(app))
            continue

        # AI fallback
        action = think(text)
        speak(action.get("response", "I didn't understand that Boss."))


if __name__ == "__main__":
    nina_loop()
