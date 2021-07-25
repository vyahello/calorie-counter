![Screenshot](media/logo.png)

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Build Status](https://api.travis-ci.com/vyahello/calorie-counter.svg?branch=master)](https://www.travis-ci.com/github/vyahello/calorie-counter)
[![Coverage Status](https://coveralls.io/repos/github/vyahello/calorie-counter/badge.svg?branch=master)](https://coveralls.io/github/vyahello/calorie-counter?branch=master)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE.md)
[![PyPI version shields.io](https://img.shields.io/pypi/v/calorie-counter.svg)](https://pypi.python.org/pypi/calorie-counter/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/calorie-counter.svg)](https://pypi.python.org/pypi/calorie-counter/)
[![PyPi downloads](https://img.shields.io/pypi/dm/calorie-counter.svg)](https://pypi.python.org/pypi/calorie-counter)
[![CodeFactor](https://www.codefactor.io/repository/github/vyahello/calorie-counter/badge)](https://www.codefactor.io/repository/github/vyahello/calorie-counter)
[![Docker pulls](https://img.shields.io/docker/pulls/vyahello/calorie-counter.svg)](https://hub.docker.com/repository/docker/vyahello/calorie-counter)

# Calorie counter
> This project represents a simple web app to calculate calories based on given food type. 

## Tools

### Production
- front-end
  - html5
  - css3
  - javascript (vanilla)
- back-end
  - python 3.6, 3.7, 3.8
  - [flask](http://flask.palletsprojects.com)

### Development
- [pytest](https://pypi.org/project/pytest/)
- [mypy](http://mypy.readthedocs.io/en/latest)
- [black](https://black.readthedocs.io/en/stable/)
- [travis](https://travis-ci.org) CI

## Usage

![Usage](media/howto.gif)

### Quick start

Please open [web site](https://food-calories-counter.herokuapp.com) to check out an application.

### Docker run

Please use the following command to run app via docker:
```bash
docker run -it -p 4000:5001 vyahello/calorie-counter:0.1.0 counter
```

Then please browse for http://0.0.0.0:4000 endpoint.

### PYPI Installation

Please run following script to obtain latest package from PYPI:
```bash
pip install calorie-counter
```
Then please execute instructions below to launch game from your environment:
```python
>>> from counter import Bind, easyrun
>>> 
>>> easyrun(Bind("0.0.0.0:5003"))
```
Then please open [localhost:5003](http://localhost:5003) endpoint in your browser.

### Source code

To be able to run source code please execute command below:
```bash
python -m counter --bind 0.0.0.0:5003 --debug
```

Also you can use **flask** built-in runner based on [.flaskenv](.flaskenv) config file: 
```bash
export FLASK_APP=counter
flask run
```

Then please open [localhost:5003](http://localhost:5003) endpoint in your browser.

## Development notes

### CI

Project has Travis CI integration using [.travis.yml](.travis.yml) file thus code analysis (`black`, `mypy`) and unittests (`pytest`) will be run automatically
after every made change to the repository.

To be able to run code analysis, please execute command below:
```bash
./analyse-code.sh
```

### Build docker images

To build base image please run the following command:
```bash
docker build --no-cache -t vyahello/calorie-counter:0.1.0 -f docker/Dockerfile .
```

To build main image please run the following command:

```bash
docker build --no-cache -t vyahello/calorie-counter:test -f docker/Dockerfile --build-arg VERSION=0.1.0 .
```

Please use the following commands to push image:
```bash
docker push vyahello/calorie-counter:test
```

### Release notes

Please check [changelog](CHANGELOG.md) file to get more details about actual versions and it's release notes.

### Meta

Author – _Volodymyr Yahello_

Distributed under the `MIT` license. See [license](LICENSE.md) for more information.

You can reach out me at:
* [vyahello@gmail.com](vyahello@gmail.com)
* [https://twitter.com/vyahello](https://twitter.com/vyahello)
* [https://www.linkedin.com/in/volodymyr-yahello-821746127](https://www.linkedin.com/in/volodymyr-yahello-821746127)

### Contributing
I would highly appreciate any contribution and support. If you are interested to add your ideas into project please follow next simple steps:

1. Clone the repository
2. Configure `git` for the first time after cloning with your `name` and `email`
3. `pip install -r requirements.txt` to install all project dependencies
4. `pip install -r requirements-dev.txt` to install all development project dependencies
5. Create your feature branch (`git checkout -b feature/fooBar`)
6. Commit your changes (`git commit -am 'Add some fooBar'`)
7. Push to the branch (`git push origin feature/fooBar`)
8. Create a new Pull Request

### What's next

All recent activities and ideas are described at project [issues](https://github.com/vyahello/calorie-counter/issues).
If you have ideas you want to change/implement please do not hesitate and create an issue.
