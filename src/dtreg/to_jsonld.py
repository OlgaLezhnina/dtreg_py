from .helpers import generate_uid
import pandas as pd
import json


def differ_input(input):
    if isinstance(input, pd.DataFrame):
        output = df_structure(input)    
    else:
        output = input
    return output

def df_structure(df):
  global uid
  global constants
  result = {}  
  result["@type"] = constants["table"]
  result["label"] = df.name if hasattr(df, "name") else "Table"  
  column_ids = []
  result["columns"] = []
  for i, col in enumerate(df.columns):  
    column = {
      "@type": constants["column"],
      "titles": col,
      "number": i + 1,
      "@id":"_:n" + str(uid())
    }
    column_ids.append(column["@id"])
    result["columns"].append(column)
  result["rows"] = []
  for i, ro in df.iterrows():
    row = {
      "@type": constants["row"],
      "number": i + 1,
      "titles": str(i + 1),
      "cells": []
    }
    for j, cel_val in enumerate(ro): 
      row["cells"].append({
        "@type": constants["cell"],
        "value": str(cel_val) if not pd.isna(cel_val) else None,          
        "column": column_ids[j]
      })     
    result["rows"].append(row)
  result["@id"] = "_:n" + str(uid()) 
  return(result)

    
def to_jsonld(instance):
    result_all = {}
    global uid
    uid = generate_uid()
    global constants
    constants = instance.add_df_constants()
    def write_info(instance):
        result = {
        "@id": "_:n" + str(uid()),
        "@type": instance.add_dt_type(instance.dt_id)}
        for field in instance.prop_list:
            instance_field = getattr(instance, field)
            prop_id = next(item for item in instance.prop_info if item["dtp_name"] == field)["dtp_id"]
            prop_type = instance.add_dtp_type(prop_id)
            if instance_field is None or instance_field is []:
                pass
            elif isinstance(instance_field, list) and hasattr(instance_field[0], "prop_list"):
                result[prop_type] = list(map(write_info, instance_field))           
            elif hasattr(instance_field, "prop_list"):
                result[prop_type] = write_info(instance_field)
            else: 
                result[prop_type] = differ_input(instance_field)
        return result
    result_all[instance.dt_name] = write_info(instance)
    result_all["@context"] = instance.add_context(instance.prefix)
    result_json = json.dumps(result_all, indent = 2)
    return result_json
