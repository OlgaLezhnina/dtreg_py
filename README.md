# dtreg
The goal of dtreg is to help the users interact with various data type registries (DTRs) and write research results in the machine-actionable format. Currently, the ePIC and the ORKG DTRs are supported. 
The user can load a DTR schema (an ePIC datatype or an ORKG template) as a Python object.
The next step is to create a new instance of the schema by filling the relevant fields.
Finally, the instance can be written as a machine-actionable JSON-LD file. 
## Example

This example shows you how to work with a DTR schema; you need to know the schema identifier.
As an example, the ePIC datatype with the DOI “<https://doi.org/21.T11969/74bc7748b8cd520908bc>" is used.
For the ORKG, please use the ORKG template URL, such as “<https://incubating.orkg.org/template/R855534>".

```{python}
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