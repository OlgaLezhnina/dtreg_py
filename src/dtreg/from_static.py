import importlib_resources
resources = importlib_resources.files("dtreg")
template_1 = resources.joinpath("src/dtreg/data", "empty_schema.json").read_text()

from importlib_resources import files
import setuptools 

data_text = files("dtreg.data").joinpath("empty_schema.json").read_text()
