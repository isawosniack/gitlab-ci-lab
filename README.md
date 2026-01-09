# How to build the documentation (locally with Sphinx):
- Create a new python venv and activate it
- Install all requirements:

``` pip install -r requirements.txt ```

- Build the sphinx documentation:
``` sphinx-build -b html docs docs/_build/html ```

- To use the esbonio extension for VSC, update the user `settigs.json`  with the following:

```
{
  "esbonio.logging.level": "debug",
  "esbonio.sphinx.pythonCommand": ["PATH TO PYTHON venv"],
  "esbonio.server.pythonPath": "PATH TO PYTHON venv",
}
```