PYTHON EXAMPLES
===============

Random Python examples and code snippets when learning Python.

Setup
-----

Versions:

* Ubuntu 14.04.5 LTS (Windows Subsystem for Linux)
* Python 3.4.3

In Ubuntu Python installation doesn't come bundled with pip but it's a separate package. Unfortunately the package is very old. Therefore [install the latest pip version manually](https://pip.pypa.io/en/latest/installing/):

```
$ curl -O https://bootstrap.pypa.io/get-pip.py
$ sudo -H python3 get-pip.py
```

Virtualenv guides:

* https://www.dabapps.com/blog/introduction-to-pip-and-virtualenv-python/
* http://docs.python-guide.org/en/latest/dev/virtualenvs/

Install virtualenv:

```
$ sudo pip install virtualenv
```

Create new virtual environment:

```
$ virtualenv env
Using base prefix '/usr'
New python executable in /mnt/d/src/python-ex/env/bin/python3
Also creating executable in /mnt/d/src/python-ex/env/bin/python
Installing setuptools, pip, wheel...done.
$
```

Activate virtualenv:

```
$ . env/bin/activate
(env)$ which python
/mnt/d/src/python-ex/env/bin/python
(env)$ python -V
Python 3.4.3
```

How to run Python
-----------------

How to compile a Python script before execution:

```
(env)$ python -m py_compile script.py && python script.py
```

How to run a Python script with a debugger:

```
(env)$ python -m pdb script.py
```
