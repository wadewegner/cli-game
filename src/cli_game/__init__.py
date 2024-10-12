from .game import main as run_game
from ._version import __version__

def run_game():
    import curses
    return curses.wrapper(main)
