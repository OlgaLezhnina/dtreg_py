# dtreg
The goal of dtreg is to help the user interact with various data type registries (DTRs).
Currently, the ePIC and the ORKG DTRs are supported.  
The user can load a DTR schema (e.g., an ePIC datatype or an ORKG template) as a Python object and create their own instance of the schema. 
This instance can be written as a machine-actionable JSON-LD file.
## Example

This example shows you how to work with a schema from a DTR; you need to
know the the identifier (URL) of the schema. The schema we use as an example belongs to
the ePIC DTR with DOI “<https://doi.org/21.T11969/74bc7748b8cd520908bc>".
For the ORKG, please use a template URL, such as “<https://incubating.orkg.org/template/R855534>".

```{python}
## import functions from the dtreg
from dtreg.load_datatype import load_datatype
from dtreg.to_jsonld import to_jsonld
## load the datatype schema you need
dt = load_datatype("https://doi.org/21.T11969/74bc7748b8cd520908bc")
## look at schemata to select the one(s) you intend to use
dt.__dict__.keys() 
## check available fields for your schema
dt.inferential_test_output.prop_list 
## create your instance by filling the fields of your choice
my_inst = dt.inferential_test_output(label = "my_results")
## write the instance in JSON-LD format
my_json = to_jsonld(my_inst) 
```
For more information, please see XXX.