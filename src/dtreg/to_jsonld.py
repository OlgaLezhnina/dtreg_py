from .helpers import generate_uid
import pandas as pd

def differ_type(input):
    if isinstance(input, pd.DataFrame):
        output = df_structure(input)    
    else:
        output = input
    return output

def df_structure(df, label):
    pass
    
def to_jsonld(instance):
    result_all = {}
    uid = generate_uid()
    context = {}
    context[instance.identifier] = ("https://doi.org/"+ instance.identifier)
    def write_info(instance):
        result = {}
        result["@id"] = "_:n" + str(uid())
        result["@label"] = instance.label
        result["@type"] = "https://doi.org/" + instance.identifier
        field_list = instance.prop_list
        for field in field_list:
            instance_field = getattr(instance, field)
            if hasattr(instance_field, "prop_list"):
                result[field] = write_info(instance_field)
            elif instance_field is None:
                pass
            else:
                result[field] = differ_type(instance_field)
        return result
    result_all[instance.name] = write_info(instance)
    result_all["@context"] = context
    return result_all
