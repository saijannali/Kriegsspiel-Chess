### Chess Symbols 
Game will use Chess symbols (♔) if they are available in the current character set. The pieces will default to letters if the unicode symbols are unavailable. 
To change the CMD encoding to UTF-8 in Windows, use the command `chcp 65001`.


### Player info
|   Color   |   ID      |   Case    |   Board   |
|-----------|-----------|-----------|-----------|
|   White   |   0       |   UPPER   |   top     |
|   Black   |   1       |   lower   |   bottom  |


### Running the game
For a list of options for running the game, run Kriegspiel.py with the -h flag.

`> python Kriegspiel.py -h`

```
usage: Kriegspiel.py [-h] [-l LAYOUT_FILE] [-r {0,1,fair,laxx}]
                     [-g {debug,pvp,testing}] [-p1 {human,random}]
                     [-p2 {human,random}]
optional arguments:
  -h, --help            show this help message and exit
  -l LAYOUT_FILE, --layout_file LAYOUT_FILE
                        The filepath of the layout you wish to load.
  -r {0,1,fair,laxx}, --referee {0,1,fair,laxx}
                        The type of referee.
  -g {debug,pvp,testing}, --gamemode {debug,pvp,testing}
                        The game mode to use.
  -p1 {human,random}, --player1 {human,random}
                        The type of player one.
  -p2 {human,random}, --player2 {human,random}
                        The type of player two.
```

The application has been tested using Windows 10 but should also run under linux and mac.