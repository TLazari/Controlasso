# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

import django

sys.path.insert(0, os.path.abspath('../..'))  # Caminho até onde está o manage.py
os.environ['DJANGO_SETTINGS_MODULE'] = 'projeto_controlasso.settings'
django.setup()

project = 'Controlasso'
copyright = '2025, 2025, Contribuintes do github'
author = '2025, Contribuintes do github'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.napoleon',
              'sphinx.ext.viewcode',
              'sphinxcontrib.mermaid',  # Para diagramas Mermaid
              'myst_parser',  # Para Markdown
              'sphinxcontrib.httpdomain', # Para documentar rotas
            ]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'pt-BR'
locale_dirs = ['locales/']  # Caminho onde ficam os .po/.mo


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']