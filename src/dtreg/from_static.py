from importlib_resources import files
template_1 = files("dtreg.data").joinpath("empty_schema.json").read_text()
