project = "Elektronik Ausbildung"
copyright = "2026"
author = "Elektroniker Ausbildung"

extensions = [
    "myst_parser",
]

myst_url_schemes = ("http", "https", "mailto", "ftp")

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_title = "Elektronik Ausbildung"

html_theme = "pydata_sphinx_theme"
html_theme_options = {
    "navigation_depth": 3,
    "show_nav_level": 2,
}
html_static_path = ["_static"]

source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}
