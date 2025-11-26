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

## `e004`

How to hide transparent dependency, so that the users (module `user`) of `modb` (module b) don't have to import `moda` (module a). 

## `e005`

Python [unit testing](https://en.wikipedia.org/wiki/Unit_testing) basics with:
* [pytest](https://pytest.org/) - 3rd party testing framework (standard library alternative is [unittest](https://docs.python.org/3/library/unittest.html))
* [doctest](https://docs.python.org/3.10/library/doctest.html) - test examples embedded in [docstrings](https://peps.python.org/pep-0257/)
* [coverage.py](https://coverage.readthedocs.io/) - test coverage
* [pytest-cov](https://pypi.org/project/pytest-cov/) - pytest plugin for coverage.py

Test layout and test discovery implements one possible set of best practices described in [Good Integration Practices](https://docs.pytest.org/en/stable/explanation/goodpractices.html).

[How to parametrize fixtures and test functions](https://docs.pytest.org/en/stable/how-to/parametrize.html#).

Activate/setup virtual environment:
```
cd e005/
source .venv/bin/activate
pip install -r requirements.txt
```

How to run tests:
```shell
# run doctests with python
python3 -m doctest --verbose src/intseqs.py
# run doctests with pytest
pytest --doctest-modules
# run doctests with pytest + test coverage
pytest src --doctest-modules --cov=src 
# run doctests and unit test with pytest + test coverage
pytest src test --doctest-modules --cov=src --cov-context=test
```

Options can be set in `pytest.toml` [configuration file](https://docs.pytest.org/en/stable/reference/customize.html).

## `e006`

Mocking in [`pytest`](https://pytest.org/) with [`pytest-mock`](https://pypi.org/project/pytest-mock/) that is just a thin wrapper around [`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html) standard library module.

See also:
* https://nedbatchelder.com/blog/201908/why_your_mock_doesnt_work.html
* https://blog.cleancoder.com/uncle-bob/2014/05/10/WhenToMock.html

Note the internet has plenty of arguments against mocking, in complex scenarios mocks seems to go out of hand easily (setup becomes complex and mocks are tightly coupled with implementation details that shouldn't matter). Use with care.

Activate/setup virtual environment:
```
cd e006/
source .venv/bin/activate
pip install -r requirements.txt
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