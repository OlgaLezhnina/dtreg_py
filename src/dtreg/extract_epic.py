from .request_dtr import request_dtr
from .helpers import range_split
from .helpers import format_string

def extract_epic(datatype_id):
    extract_all = {}
    def extractor_function(datatype_id):
        info = request_dtr(datatype_id + "?locatt=view:json")
        schema_dict = {
            "dt_name": format_string(info["name"]),
            "dt_id": info["Identifier"].split("/", 4)[1],
            "dt_class": info["Schema"]["Type"]}
        extracted = [[schema_dict]]
        all_props = []
        for prop in info["Schema"].get("Properties", []):
            if "Type" in prop:
                card = range_split(prop["Properties"]["Cardinality"])
                specific_prop_dict = {
                    "dtp_name": format_string(prop["Name"]),
                    "dtp_id": info["Identifier"] + "#" + format_string(prop["Name"]),
                    "dtp_card_min": card["min"],
                    "dtp_card_max": card["max"],
                    "dtp_value_class": prop["Type"]}
                extractor_function("https://doi.org/" + prop["Type"])
            else:        
                specific_prop_dict = {
                    "dtp_name": format_string(prop["Property"]),
                    "dtp_id": info["Identifier"] + "#" + format_string(prop["Property"]),
                    "dtp_card_min": None,
                    "dtp_card_max": None,
                    "dtp_value_class": prop["Value"]}   
            all_props.append(specific_prop_dict)
        extracted.append(all_props)
        extract_all[schema_dict["dt_name"]] = list(extracted) 
    extractor_function(datatype_id)
    return(extract_all)