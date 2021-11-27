# CumBot v0.2.0

A Discord Bot for my highschool friends (using [discord.py](https://pypi.org/project/discord.py/)).

Written in [Python 3](https://www.python.org/downloads/).

## Sections
- [Available commands](#available-commands)
- [Getting started](#getting-started)
- [Virtual environment](#virtual-environment)

---

## Available Commands:

- To get help: `!help`.
- To learn more about a command: `!help <command_name>`.

| Command      | Argument(s)                                                            | Definition                                              |
|--------------|------------------------------------------------------------------------|---------------------------------------------------------|
| `!joke`      | *None* OR `any`,`misc`,`programming`,`dark`,`pun`,`spooky`,`christmas` | Tells a joke depending on the category or a random one. |                                       
| `!math`      | Mathematical expression. Eg: `1+1`                                     | Calculate a mathematical expression.                    |
| `!jew`       | *None*                                                                 | Summon Eli.                                             |
| `!crackhead` | *None*                                                                 | Summon Felix.                                           |
| `!loser`     | *None*                                                                 | Summon Cedric.                                          |
| `!sale`      | *None*                                                                 | *REDACTED*                                              |
| `!jizz`      | *None*                                                                 | *REDACTED*                                              |
| `!fuckyou`   | *None*                                                                 | *REDACTED*                                              |
| `!oleg`      | *None*                                                                 | *REDACTED*                                              |

## Getting Started
1. Clone the project: https://github.com/cedricouellet/cum_bot.git
2. Copy `.example.env` to a `.env` file
3. Fill out the required fields in `.env` (given from your [Discord Developper Portal](https://discord.com/developers/applications))
4. Install [Python 3](https://www.python.org/downloads/)
5. **Optional:** [Setup a virtual environment](#virtual-environment)
6. Install required pip modules: `pip install -r requirements.txt`
7. Run the program:`python3 __main__.py`

And you're good to go!

## Virtual Environment

Using a virtual environment makes things much cleaner and easier.

You don't need to install pip dependencies on your local machine, can delete the environment once you're done with it.

- First, you need to have [Python 3](https://www.python.org/downloads/) installed.
- Then, you need to install the [virtualenv](https://pypi.org/project/virtualenv/) module: `pip install virtualenv`

### Setup & Activation

After activating the environment, you can proceed to the next step in [Getting started](#getting-started).

#### Windows
```shell
C:\Users\user\...\cum_bot> virtualenv venv -p python3
...
C:\Users\user\...\cum_bot> .\venv\Scripts\activate
```

#### Linux
```shell
user@host:~/../cum_bot$ virtualenv venv -p python3
...
user@host:~/../cum_bot$ . venv/bin/activate
```
### Deactivation

Once you are done developping and need to exit the virtual environment, you can execute this command to do so.

#### Windows
```shell
(venv) C:\Users\user\...\cum_bot> deactivate
```

#### Linux
```shell
(venv) user@host:~/.../cum_bot$ deactivate
```