[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

[![Build Status](https://travis-ci.org/vyahello/calorie-counter.svg?branch=master)](https://travis-ci.org/vyahello/calorie-counter)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/calorie-counter/badge.svg?branch=master)](https://coveralls.io/github/vyahello/calorie-counter?branch=master)
[![Forks](https://img.shields.io/github/forks/vyahello/calorie-counter)](https://github.com/vyahello/calorie-counter/network/members)
[![Stars](https://img.shields.io/github/stars/vyahello/calorie-counter)](https://github.com/vyahello/calorie-counter/stargazers)
[![Issues](https://img.shields.io/github/issues/vyahello/calorie-counter)](https://github.com/vyahello/calorie-counter/issues)
[![GitHub watchers](https://img.shields.io/github/watchers/vyahello/calorie-counter.svg)](https://GitHub.com/vyahello/calorie-counter/graphs/watchers/)
[![GitHub contributors](https://img.shields.io/github/contributors/vyahello/calorie-counter.svg)](https://GitHub.com/vyahello/calorie-counter/graphs/contributors/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)

[![PyPI version shields.io](https://img.shields.io/pypi/v/calorie-counter.svg)](https://pypi.python.org/pypi/calorie-counter/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/calorie-counter.svg)](https://pypi.python.org/pypi/calorie-counter/)

# Calorie counter
> This project represents simple web app to calculate calories based on given food type. 
>
> Please check https://food-calories-counter.herokuapp.com get familiar with application itself.
>
> ![Screenshot](counter/static/img/demo.png)

## Tools
- front-end
  - html5
  - css3
  - javascript (vanilla)
- back-end
  - python 3.6 | 3.7 | 3.8
  - [flask](http://flask.palletsprojects.com)
- code analysis
  - [pytest](https://pypi.org/project/pytest/)
  - [mypy](http://mypy.readthedocs.io/en/latest)
  - [black](https://black.readthedocs.io/en/stable/)

## Usage

### PYPI

Please run following script to obtain latest package from PYPI:
```bash
➜ pip install calorie-counter
```
Then please execute instructions below to launch game from your environment:
```python
from counter import Bind, easyrun

easyrun(bind=Bind("0.0.0.0:5003"), debug=True)
Running on https://0.0.0.0:5003 (CTRL + C to quit)
...
```
Then please open [localhost:5003/](http://localhost:5003/) endpoint.

### Source code

To be able to run source code please execute command below:
```bash
➜ python -m counter run --bind 0.0.0.0:5003 --debug
Running on https://0.0.0.0:5003 (CTRL + C to quit)
...
```

Also you can use **flask** built-in runner based on [.flaskenv](.flaskenv) config file: 
```bash
➜ flask run
Serving Flask app "counter/__main__.py"
...
```

For both cases, then please open [localhost:5003/](http://localhost:5003/) endpoint.

## Development notes

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `mypy`) and unittests (`pytest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
➜ ./analyse-code.sh
```

### Release notes

* 0.1.0
  * Introduce PYPI package

### Meta

Author – Volodymyr Yahello

Distributed under the `MIT` license. See [LICENSE](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://github.com/vyahello](https://github.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
1. clone the repository
2. configure Git for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all dev project dependencies

