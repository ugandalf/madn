# madn
Python implementation of a board game "Mensch ärgere Dich nicht" or "Ludo".
Originally made for a python course at University of Wrocław.
Uses matplotlib for graphics, pdoc3 for documentation, UMLet for UML diagrams, unittest for tests.

Needs some polishing:
- [ ] Game might be too fast - implement slower mode?
- [ ] Require only one window open instead of matplotlib one and terminal for input -> input in matplotlib
- [ ] Examine glitched graphics when switching to another window in XMonad until window is updated
- [ ] Add requirements.txt for reproducible builds
- [ ] Commandline arguments for parsing Config
- [ ] Documentation links as described in https://pdoc3.github.io/pdoc/doc/pdoc/#linking-to-other-identifiers
- [ ] Make the game prettier
- [ ] Describe all in better detail, in particular how many players are supported, squares per player, player shapes etc.
- [ ] Better gameplay? AI options? Expand on dice rolls? Embed in another window?
