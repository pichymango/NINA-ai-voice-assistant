import os
import re
from speech import speak
from datetime import datetime

def process_command(command: str) -> bool:
    command = command.lower()
    print("DEBUG:", repr(command))

    # EXIT
    if "exit" in command or "stop" in command:
        speak("Goodbye")
        return False

    # HELLO
    if "hello" in command:
        speak("Hello Archit")
        return True

    # TIME
    if "time" in command:
        now = datetime.now().strftime("%I:%M %p")
        speak(f"The time is {now}")
        return True

    # DATE
    if "date" in command:
        today = datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
        return True

    # OPEN SAFARI
    if "open safari" in command or "open browser" in command:
        speak("Opening Safari")
        os.system("open -a Safari")
        return True

    # OPEN VS CODE
    if "open vs code" in command or "open vscode" in command:
        speak("Opening Visual Studio Code")
        os.system("open -a 'Visual Studio Code'")
        return True

    # CALCULATOR
    if command.startswith("calculate"):
        expression = command.replace("calculate", "").strip()

        expression = (
            expression
            .replace("plus", "+")
            .replace("minus", "-")
            .replace("times", "*")
            .replace("multiply", "*")
            .replace("multiplied by", "*")
            .replace("divide", "/")
            .replace("divided by", "/")
            .replace("six", "6")
            .replace("three", "3")
            .replace("eight", "8")
            .replace("five", "5")
        )

        expression = re.sub(r"[^0-9+\-*/(). ]", "", expression)

        try:
            result = eval(expression)
            speak(f"The answer is {result}")
        except:
            speak("Sorry, I could not calculate that")

        return True

    speak("I did not understand that")
    return True
