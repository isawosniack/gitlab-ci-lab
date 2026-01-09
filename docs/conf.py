# -- Project information
project = "gitlab-ci-lab"
copyright = "2026, Isabella Wosniack"
author = "Isabella Wosniack"
release = "1.0"

# -- General configuration
extensions = [
        "sphinx.ext.intersphinx", 
        "sphinx_design", 
        "myst_parser",
        "sphinx_copybutton",
        "sphinxcontrib.mermaid"
      ]

html_title = "GitLab CI & Docker"
templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Options for HTML output
html_theme = "sphinx_rtd_theme"
html_title = "Esbonio Demo"
