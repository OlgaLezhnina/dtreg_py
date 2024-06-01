from .request_dtr import request_dtr
from dtreg.helpers import range_split

def extract_epic(dt_id):
    extract_all = {}
    def extractor_function(dt_id):
        info = request_dtr(dt_id + "?locatt=view:json")
        schema_dict = {
            "dt_name": info["name"],
            "dt_id": info["Identifier"],
            "dt_class": info["Schema"]["Type"]}
        extracted = [[schema_dict]]
        all_props = []
        for prop in info["Schema"].get("Properties", []):
            card = range_split(prop["Properties"]["Cardinality"])
            if "Type" in prop:
                specific_prop_dict = {
                    "dtp_name": prop["Name"],
                    "dtp_id": info["Identifier"] + "#" + prop["Name"],
                    "dtp_card_min": card["min"],
                    "dtp_card_max": card["max"],
                    "dtp_value_class": prop["Type"]}
                extractor_function("https://doi.org/" + prop["Type"])
            else:        
                specific_prop_dict = {
                    "dtp_name": prop["Property"],
                    "dtp_id": info["Identifier"] + "#" + prop["Property"],
                    "dtp_card_min": None,
                    "dtp_card_max": None,
                    "dtp_value_class": prop["Value"]}   
            all_props.append(specific_prop_dict)
        extracted.append(all_props)
        extract_all[schema_dict["dt_name"]] = list(extracted) 
        return(extract_all)
    extractor_function(dt_id)
    return(extract_all)