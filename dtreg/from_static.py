from importlib.resources import files
template_1 = files('dtreg.templates').joinpath('empty_schema.json').read_text()