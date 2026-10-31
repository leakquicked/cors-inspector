![Python checks](https://github.com/leakquicked/cors-inspector/actions/workflows/python-checks.yml/badge.svg)

# CORS Inspector

Review copied CORS response headers for permissive combinations.

## Requirements
Python 3.10+, standard library only.

## Usage
`python cors_inspector.py --help`

Supply a local text export or copied response headers. This tool is passive: it does not contact websites or alter configuration. Findings are advisory and require review in context.

## Tests
`python -m unittest discover -s tests -v`
