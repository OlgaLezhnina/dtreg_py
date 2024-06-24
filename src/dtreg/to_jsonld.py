from .helpers import generate_uid
import pandas as pd
import json


def differ_type(input):
    if isinstance(input, pd.DataFrame):
        output = df_structure(input)    
    else:
        output = input
    return output

def df_structure(df):
  global uid
  result = {}  
  result["@type"] = "https://doi.org/21.T11969/0424f6e7026fa4bc2c4a"
  result["label"] = df.name if hasattr(df, "name") else "Table"  
  column_ids = []
  result["columns"] = []
  for i, col in enumerate(df.columns):  
    column = {
      "@type": "https://doi.org/21.T11969/65ba00e95e60fb8971e6",
      "titles": col,
      "number": i + 1,
      "@id":"_:n" + str(uid())
    }
    column_ids.append(column["@id"])
    result["columns"].append(column)
  result["rows"] = []
  for i, ro in df.iterrows():
    row = {
      "@type": "https://doi.org/21.T11969/9bf7a8e8909bfd491b38",
      "number": i + 1,
      "titles": str(i),
      "cells": []
    }
    for j, cel_val in enumerate(ro): 
      row["cells"].append({
        "@type":"https://doi.org/21.T11969/4607bc7c42ac8db29bfc",
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
    context = {}
    context["doi:"] = "https://doi.org/"
    def write_info(instance):
        result = {
        "@id": "_:n" + str(uid()),
        "@type": "doi:" + instance.dt_id}
        for field in instance.prop_list:
            instance_field = getattr(instance, field)
            if instance_field is None or instance_field is []:
                pass
            elif isinstance(instance_field, list) and hasattr(instance_field[0], "prop_list"):
                result[field] = list(map(write_info, instance_field))           
            elif hasattr(instance_field, "prop_list"):
                result[field] = write_info(instance_field)
            else: 
                result[field] = differ_type(instance_field)
        return result
    result_all[instance.dt_name] = write_info(instance)
    result_all["@context"] = context
    result_json = json.dumps(result_all, indent = 2)
    return result_json
