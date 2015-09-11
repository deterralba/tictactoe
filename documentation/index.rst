.. TicTacToe documentation master file, created by
   sphinx-quickstart on Sun Sep  6 13:16:10 2015.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to TicTacToe's documentation!
=====================================

Forewords
---------

**Dear reader,**

This is the cherish documentation of my TicTacToe program.
I made this program with love and patience to learn how the use of a bunch of new technologies.

For instance, the doc you are currently reading is compiled with sphinx, a very powerful and
noob-unfriendly software.

Let's go to the point!
----------------------

If you are in a hurry, please go the the :mod:`main` module page.
Everything is explained there if you just want to run a quick simulation.

Contents:
---------

The project is divided in several packages. They are all called from the main module located
at the root of the project.

The :mod:`core` package provides... the core classes of the program, which represent a game, the board,
the manager of a simulation, basic players etc.

The :mod:`players` package contains more sophisticated players that have either simple strategies
or are able to learn from the past game!
It is in this package that you should create your own players.

The :mod:`misc` package (aka *miscellaneous*) contains other useful packages, for instance the one used to
plot graphs of simulations' results.


.. toctree::
   :maxdepth: 2

   pages/main
   pages/modules
   pages/trash


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

