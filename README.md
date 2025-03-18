# Python Examples

Currently I'm working with version [3.10](https://devguide.python.org/versions/).

Random Python examples and code snippets when learning Python.

* `e*` - subdirectories of more "complex" examples that might also need their own virtual environment.
* `p*.py` - simple snippets/scripts that are expected to be run on your vanilla Python interpreter.
* `server.py` - very simple HTTP server for logging requests. Downloaded from [mdonkers/server.py](https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7).

## `e003`

Python package example how to create a standalone Python applications for easier delivery with:

* [pyinstaller](https://pyinstaller.org/en/stable/)
  * TODO: not tried yet as zipapp was good enough for me atm.
  * Packages also Python interpreter.
  * Packages are operating system specific.
  * A separate package.
* [zipapp](https://docs.python.org/3/library/zipapp.html)
  * Doesn't include Python interpreter, runtime has to have compatible version of the interpreter.
  * Part of Python standard library.

Two simple programs having dependency to external [Jinja2](https://pypi.org/project/Jinja2/) PyPI module.

Activate/setup virtual environment:
```
cd e003/
source .venv/bin/activate
pip install -r requirements.txt
```

Run the programs:
```
python src/program1.py
python src/program2.py
```

Package the programs as executable Python zip archives (zipapp):
```
pip install -r requirements.txt --target src/
python -m zipapp -m program1:main -o program1.pyz src/
python -m zipapp -m program2:main -o program2.pyz src/
```

Or see `Makefile`.

Copy the archives somewhere and run with compatible Python interpreter:
```
python3 program1.pyz
python3 program2.pyz
```

## Virtual Environment 101

Guides:
* https://docs.python.org/3/tutorial/venv.html

Create virtual environment:
```
python3 -m venv .venv
```
Activate virtual environment:
```
source .venv/bin/activate
```
Install dependencies into virtual environment (the first time):
```
pip install PACKAGE
```
Install dependencies into virtual environment (subsequent times):
```
pip install -r requirements.txt
```
Freeze dependencies:
```
pip freeze > requirements.txt
```
Run:
```
python MODULE.py PARAMETERS...
```

## How to run Python

How to compile a Python script before execution:
```
(.venv)$ python -m py_compile <SCRIPT> && python <SCRIPT>
```

How to run a Python script with a debugger:
```
(.venv)$ python -m pdb <SCRIPT>
```

## How to reload a module in REPL

Use [`importlib.reload()`](https://docs.python.org/3/library/importlib.html#importlib.reload):
```
>>> import <MODULE>
>>> import importlib
>>> importlib.reload(<MODULE>)
```