import webbrowser
import requests
import re
import subprocess
from urllib.parse import quote_plus


# ---------- OPEN WEBSITE ----------
def open_website(url: str) -> str:
    if not url.startswith("http"):
        url = "https://" + url

    webbrowser.open(url)
    return f"Opening {url}"


# ---------- SEARCH GOOGLE ----------
def search_web(query: str) -> str:
    encoded = quote_plus(query)
    url = f"https://www.google.com/search?q={encoded}"
    webbrowser.open(url)
    return f"Searching Google for {query}"


# ---------- PLAY YOUTUBE VIDEO (AUTO PLAY) ----------
def play_youtube(query: str) -> str:
    query = query.strip()
    encoded_query = quote_plus(query)

    search_url = f"https://www.youtube.com/results?search_query={encoded_query}"

    try:
        html = requests.get(search_url, timeout=5).text
        match = re.search(r"watch\?v=([a-zA-Z0-9_-]{11})", html)

        if match:
            video_id = match.group(1)
            watch_url = f"https://www.youtube.com/watch?v={video_id}&autoplay=1"
            webbrowser.open(watch_url)
            return f"Playing {query} on YouTube"

        webbrowser.open(search_url)
        return f"Showing YouTube results for {query}"

    except Exception:
        webbrowser.open(search_url)
        return f"Showing YouTube results for {query}"


# ---------- CLOSE BROWSER ----------
def close_browser(browser="Safari") -> str:
    subprocess.run([
        "osascript", "-e",
        f'tell application "{browser}" to quit'
    ])
    return f"Closing {browser}"


# ---------- CLOSE CURRENT TAB ----------
def close_tab(browser="Safari") -> str:
    subprocess.run([
        "osascript", "-e",
        f'''
        tell application "{browser}"
            tell front window to close current tab
        end tell
        '''
    ])
    return "Closing current tab"
