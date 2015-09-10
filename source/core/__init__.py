"""
This is the Core package of the Game, it contains the primary classes of the game that are all needed to start
a series a game between two random players.

Importation
===========
The clean way to import the core package is::

    from core import *

This may seem like a bad idea but the importation process in controlled in the __init__.py file.
The following classes will be imported:

- BoardAndRules
- BoardState
- Game
- InteractionLevel
- Movement
- Player
- PlayerStatistic
- Simulation

Use
===
To use the imported classes, just write Game(), no need to use core.Game.Game().
This is made possible thanks to the addition of the core/ folder path to the Python path
and the use of::

    from Game import Game

in the __init__.py file.

"""


# this file is executed when a module from this folder (core) is called outside from this folder,
# for example when the doc is compiled, or in source/main.py


# Explanations: Why import the core/ path to the Python Path ?
# ============================================================
# It is far easier to manage the core package if its path is in the Python Path:
# It is possible to write "from BoardState import BoardState" in core/BoardAndRules.py (when executed from source/)
# while it should be "from core.BoardState import BoardState" if the path wasn't added.
# But "from core.BoardState import BoardState" would be problematic when executed from core/ !
# With the core path added, "from BoardState import BoardState" works when executed from both source/ and  code/.
# Tadam !

# the folder path is added to the python path
import os
import sys
sys.path.insert(0, os.path.dirname(__file__))
print("*** source/core/__init__.py is executed, source/core/ was added to the python path")
# this allows to use foo instead of core.foo in source/ (see explanations)


# the following bloc allows "from core import *" (in source/) to import directly BoardAndRules
# and not BoardAndRules.BoardAndRules (same idea for all the classes)

from BoardAndRules import BoardAndRules
from BoardState import BoardState
from Game import Game
from InteractionLevel import InteractionLevel
from Movement import Movement
from Player import Player
from PlayerStatistic import PlayerStatistic
from Simulation import Simulation

