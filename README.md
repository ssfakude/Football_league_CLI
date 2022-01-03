# Football_league
league is a cli tool to return points of a league games


## How to Install
1. `git clone https://github.com/ssfakude/Football_league_CLI.git`
2. `cd league`
3. `pip install --editable .`
4. `league`

## league

The input contains results of games, one per line. See “Sample input” for details.
The output should be ordered from most to least points, following the format specified in
“Expected output”.

__Sample input:__

```
Lions 3, Snakes 3
Tarantulas 1, FC Awesome 0
Lions 1, FC Awesome 1
Tarantulas 3, Snakes 1
Lions 4, Grouches 0

```
__Expected output:__
```
1. Tarantulas , 6 pts
2. Lions , 5 pts
3. FC Awesome , 1 pts
4. Snakes , 1 pts
5. Grouches , 0 pts
```

```commandline
Usage: league [OPTIONS] COMMAND [ARGS]...

  league information

Options:
  -f, --file_name TEXT  Input file name.  [default: input.txt]
  --help               Show this message and exit.

Command:
  league   Show points of all the teams

```

___options___
* `-f` `--file_name` - override the default location. ` league -f <league_matches_filename>`



```commandline
$ league -f input.txt

1. Tarantulas , 6 pts
2. Lions , 5 pts
3. FC Awesome , 1 pts
4. Snakes , 1 pts
5. Grouches , 0 pts
```
