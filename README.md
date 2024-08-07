# dtreg
The goal of dtreg is to help the users interact with various data type registries (DTRs) and create machine-readable data. 
Currently, we support the [ePIC](https://fc4e-t4-3.github.io/) and the [ORKG](https://orkg.org/) DTRs.
* First, load a DTR schema (an ePIC datatype or an ORKG template) as a Python object.
* Then, create a new instance of the schema by filling in the relevant fields.
* Finally, write the instance as a machine-readable JSON-LD file. 
## Example

This example shows you how to work with a DTR schema; you need to know the schema identifier.
As an example, we use the ePIC datatype with the DOI <https://doi.org/21.T11969/74bc7748b8cd520908bc>.
For the ORKG, please use the ORKG template URL, such as <https://incubating.orkg.org/template/R855534>.

```python
## import functions from the dtreg
from dtreg.load_datatype import load_datatype
from dtreg.to_jsonld import to_jsonld
## load the schema you need
dt = load_datatype("https://doi.org/21.T11969/74bc7748b8cd520908bc")
## look at the schemata to select the one(s) you intend to use
dt.__dict__.keys() 
## check available fields for your schema
dt.inferential_test_output.prop_list 
## create your instance by filling the fields of your choice
my_inst = dt.inferential_test_output(label = "my_results")
## write the instance in JSON-LD format
my_json = to_jsonld(my_inst) 
```
For more information, please see XXX.