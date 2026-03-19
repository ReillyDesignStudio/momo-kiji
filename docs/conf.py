# Configuration file for the Sphinx documentation builder.

project = "momo-kiji"
copyright = "2026, ReillyDesignStudio"
author = "ReillyDesignStudio"
release = "0.1.0"

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.duration",
    "sphinx_rtd_theme",
    "myst_parser",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# ReadTheDocs theme
html_theme = "sphinx_rtd_theme"
html_theme_options = {
    "logo_only": False,
    "display_version": True,
    "prev_next_buttons_location": "bottom",
    "style_external_links": False,
    "vcs_pageview_mode": "",
    "style_nav_header_background": "#d4693a",
}

html_static_path = ["_static"]

# MyST parser for Markdown support
source_suffix = {
    ".rst": None,
    ".md": "markdown",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
    "smartquotes",
    "tasklist",
]

# Intersphinx mapping
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
}

# HTML output
html_logo = None
html_favicon = None
html_title = "momo-kiji – CUDA for Apple Neural Engine"
html_last_updated = True
html_use_opensearch = "https://momo-kiji.readthedocs.io"
