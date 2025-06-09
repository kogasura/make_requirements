import os
import sys
sys.path.insert(0, os.path.abspath('../src'))

project = 'my_project'
author = 'AI'
release = '0.0.1'

extensions = []
templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']
