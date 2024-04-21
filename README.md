# dtreg
The goal of dtreg is to help the user interact with various data type registries (DTRs). 
The user can load a DTR schema as a Python object and create their own instance of the schema. 
This instance can be written as a machine-actionable JSON-LD file.
## Example

This example shows you how to work with a schema from a DTR; you need to
know the DOI of the schema. The schema we use as an example belongs to
the ePIC DTR with DOI
“<https://doi.org/21.T11969/74bc7748b8cd520908bc>”.

```{python}
from dtreg.load_objects import load_objects
dt = load_objects("https://doi.org/21.T11969/74bc7748b8cd520908bc")
dt.__dict__.keys() 
dt.inferential_test_output.prop_list 
my_inst = dt.inferential_test_output(label = "my_results")
```
For more information, please see XXX.