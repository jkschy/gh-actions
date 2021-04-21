Two tasks:

`doctest` task - Run `python3 -m doctest main.py` for each of Python 3.5, 3.6, 3.7, and 3.8.
`lint` task - Run `flake8 main.py` against Python 3.5

Note: main.py requires access to the `markdown` module, which is not installed by default. We need to ensure that it is installed before we run the doctests.
