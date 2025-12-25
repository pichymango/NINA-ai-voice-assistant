import webbrowser
import urllib.parse

def open_location(place: str):
    if not place:
        return "Please tell me a location."

    query = urllib.parse.quote(place)
    url = f"https://www.google.com/maps/search/{query}"
    webbrowser.open(url)

    return f"Showing {place} on maps"
