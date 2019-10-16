Welcome to *The Death of Tiffany Valencia*, a text based murder mystery
developed by Khalid Hussain and Elwood Olson, and is an adaption of the text based adventure game *Zork* by Tim Anderson, Marc Blank, Bruce Daniels, and Dave Lebling.

This program is currently stable, and we believe all bugs have been eliminated.

# Directions #

To interact with the game, the user inputs a variety of verb-noun commands. The
following commands are supported:

- `go [direction]` - Allows player to got to a specific room.
- `examine [object]` - Allows player to examine a specific object seen in the room.
- `observe` - Command to look around the room, and find objects that are present within it.
- `pickup [object]` - Allows player to pickup an object seen in the room and put in their pocket.
- `light [object]` - Allows player to "light" an object see in the room. [Note: only supported for one specific object]
- `open [object]` - Allows player to "open" some object(s) [Note: Also only supported for specific objects]
- `translate [object]` - Allows player to "translate" an object
- `quit` - Allows user to quit the game when entered, and program will exit.
- `cheat code` - Allows user to bypass the win conditions of the game (only for debugging).

If a command is not understood/not applicable, a message will appear stating so.

# Examples #

```
If you go east ==> Living Room
>>go east
Living Room
Description: A room with a nice T.V. and a coffee table.
There is an Italian-English dictionary on the table, and the same
blood trail from the Foyer leads to the bedroom...
>>observe
In the room, you observe these things:
bookshelf
betting-slip
cigarette
```

# Files #
## `final.py` ##
This is the file that needs to be executed in order to launch the game, and also contains the source code for the game.
## `game_data.txt` ##
This file contains all of the descriptions for the game that are printed on screen.
## `intro.txt` ##
This just contains the introduction that is printed on screen when `final.py` is executed.

**Note: All three files need to be in the same folder in order for the program to be executed from `final.py` properly.**

# Acknowledgments #
To the aforementioned creators of *Zork*, who have created a visually simplistic yet enjoyable adventure game for many, and whose idea for a text based game is the basis for our project. 
