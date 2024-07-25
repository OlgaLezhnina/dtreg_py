# dtreg
The goal of dtreg is to help the users interact with various data type registries (DTRs) and write research results in the machine-actionable format. 
Currently, the [ePIC](https://fc4e-t4-3.github.io/) and the [ORKG](https://orkg.org/) DTRs are supported.
First, a DTR schema (an ePIC datatype or an ORKG template) is loaded as a Python object.
Then, a new instance of the schema is created by filling in the relevant fields.
Finally, the instance is written as a machine-actionable JSON-LD file. 
## Example

This example shows you how to work with a DTR schema; you need to know the schema identifier.
As an example, the ePIC datatype with the DOI <https://doi.org/21.T11969/74bc7748b8cd520908bc> is used.
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