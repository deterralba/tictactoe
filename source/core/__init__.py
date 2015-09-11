"""
This is the Core package of the Game, it contains the primary classes of the game that are all needed to start
a series of games between two random players.

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
To use the imported classes, just write::

    game = Game()
    bAndR = BoardAndRules()  # etc...


no need to use ``core.Game.Game()``.

This is made possible thanks to the use of ``from core.Game import Game`` in the :file:`__init__.py` file.
"""


# this file is executed when a module from this folder (core) is called outside from this folder,
# for example when the doc is compiled, or in source/main.py


# Explanations: Why not importing the core/ path to the Python Path ?
# ===================================================================
# Because every module (.py file) should be executed from the source/ folder (ex: python -m core.Game)
# Hence the importation of the core/ path is not useful

# the following bloc allows "from core import *" (in source/) to import directly BoardAndRules
# and not core.BoardAndRules (same idea for all the classes)

from core.BoardAndRules import BoardAndRules
from core.BoardState import BoardState
from core.Game import Game
from core.InteractionLevel import InteractionLevel
from core.Movement import Movement
from core.Player import Player
from core.PlayerStatistic import PlayerStatistic
from core.Simulation import Simulation
