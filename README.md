# Python Examples

Random Python examples and code snippets when learning Python.

## Setup

Note that in VirtualBox setup venv can't be used as it can't create the neccessary links.

Versions:
* Lubuntu 22.04 LTS
* Python 3.10

Lubuntu Python3 installation doesn't come bundled with pip but it's a separate package:
```
sudo apt install python3-pip
```

Virtualenv guides:
* https://docs.python.org/3/tutorial/venv.html

Install virtualenv:
```
$ sudo apt install python3.10-venv
```

Create new virtual environment:
```
$ python3 -m venv .venv
```

Activate virtual environment:
```
$ source .venv/bin/activate
(.venv) $ which python
<ROOT>/.venv/bin/python
(.venv) $ python --version
Python 3.10.6
```

## How to run Python

How to compile a Python script before execution:
```
(.venv)$ python -m py_compile script.py && python script.py
```

How to run a Python script with a debugger:
```
(.venv)$ python -m pdb script.py
```
