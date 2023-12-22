<!-- Update this link with your own project logo -->
# <img src="https://raw.githubusercontent.com/Cutwell/readme-template/main/logo.png" style="width:64px;padding-right:20px;margin-bottom:-8px;"> README Template
 A template project for sharing Python projects on GitHub.

<!-- Find new badges at https://shields.io/badges -->
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

- This project contains templates you can use to write your own `README`, `CONTRIBUTING` and `PULL_REQUEST_TEMPLATE` files.
- It also includes a simple Python CLI tool and `requirements.txt` file as a small demo.
	- The demo uses the [on-this-day](https://byabbe.se/on-this-day/#) public API to list events Wikipedia associates with a given month and day.

[![Demo of the "on this day" app in the terminal. The user asks for events that have occured on the 6th of February and the program outputs a list from Wikipedia.](demo.gif)](https://github.com/faressoft/terminalizer)

## Install dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. Run the program from the command line like this:

- The first argument is the month (1-12).
- The second argument is the day (1-31).

E.g.:

```sh
python3 src/on_this_day.py 2 6
```

## Contributing

<!-- Remember to update the links in the `.github/CONTRIBUTING.md` file from `Cutwell/readme-template` to your own username and repository. -->

For information on how to set up your dev environment and contribute, see [here](.github/CONTRIBUTING.md).

## License

MIT
