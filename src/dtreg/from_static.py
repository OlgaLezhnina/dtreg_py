import importlib_resources
resources = importlib_resources.files("dtreg")
template_1 = resources.joinpath("src/dtreg/data", "empty_schema.json").read_text()
