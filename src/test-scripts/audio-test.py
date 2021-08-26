import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from player import Player

player = Player()
player.play(["files/start.mp3"])

input("Press Enter stop...")
