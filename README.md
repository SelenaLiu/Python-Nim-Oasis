# The Nim Oasis
A short Python project that allows the user to play Nim with the terminal interface. Project time: 3 days / 5 hours

Currently, the game still needs improvement, but is at a stage where one can play a number of different games.
Default number of piles allowed for both singleplayer and multiplayer is 3. Player wins if their opponent is forced to remove
the last value amongst all piles.

## Single player Mode
This was the most difficult part of the project. The computer player is designed to search for a winning move at all times 
by reducing the nim sum to 0. The winning strategy I followed can be found [here](https://plus.maths.org/content/play-win-nim).

If the computer is at a losing position, it is recognized, but instead of making the best possible move, it will choose randomly.
This may be improved on in the future, but for now, it allows for a fun game with the innocent player. The number of piles cannot
be changed. (This may change as well).

## Multiplayer Mode
This allows for 2 and only 2 players. With this mode, you may choose how many piles you would like to play with, with a minimum
limit of 2 and a maximum of 10. Players take turns removing from piles until the game ends when there is either only 1 left
out of all three piles, or if the player committed virtual suicide by removing all the remaining values in all piles.

## Libraries + Technical details
I used random.py, in particular - random.randrange(min, max, step)

Cool functions that made the whole process easier include bin(integer) and sum(array)
I was also able to sneak in a recursive function.

Overall, was focused more on simplification, organization, and a reminder of basic Python conventions.
