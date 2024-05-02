import pandas as pd

def differ_type(input):
    if isinstance(input, pd.DataFrame):
        output = df_structure(input)    
    elif input is None:
        output = None
    else:
        output = list(input)
    return output

def df_structure(df, label):
    return None
    
def to_jsonld(instance):
    result_all = {}
    def write_info(instance):
        result = {}
        result["label"] = instance.label
        field_list = instance.prop_list
        for field in field_list:
            instance_field = getattr(instance, field)
            if hasattr(instance_field, "prop_list"):
                print(instance_field)
                result[field] = list(write_info(instance_field))
            else:
                result[field] = "dunno"
        return result
    result_all[instance.identifier] = write_info(instance)
    return result_all
