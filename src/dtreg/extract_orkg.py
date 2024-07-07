from .request_dtr import request_dtr
from .helpers import format_string

def extract_orkg(datatype_id):
    part = datatype_id.split("/", 4)
    orkg_hostname = part[0] + "//" + part[2]
    resource_id = part[4]
    extract_all = {}
    def extractor_function(resource_id):
        info = request_dtr(orkg_hostname + "/api/templates/" + resource_id)
        schema_dict = {
            "dt_name": format_string(info["label"]),
            "dt_id": info["id"],
            "dt_class": info["target_class"]["id"]}
        extracted = [[schema_dict]]
        all_props = []
        for prop in info.get("properties", []):
            specific_prop_dict = {
                "dtp_name": format_string(prop["path"]["label"]),
                "dtp_id": prop["path"]["id"],
                "dtp_card_min": prop["min_count"],
                "dtp_card_max": prop["max_count"]
                }
            if "class" not in prop:
                specific_prop_dict["dtp_value_class"] = prop["datatype"]["id"]
            else:        
                specific_prop_dict["dtp_value_class"] = prop["class"]["id"]
                info_n = request_dtr(orkg_hostname + "/api/templates/?target_class=" + prop["class"]["id"])
                if len(info_n["content"]) > 0:
                   nested_id = info_n["content"][0]["id"]
                   nested_name = info_n["content"][0]["label"]
                   if nested_name not in extract_all:
                       extractor_function(nested_id)
            all_props.append(specific_prop_dict)
        extracted.append(all_props)
        extract_all[schema_dict["dt_name"]] = list(extracted) 
    extractor_function(resource_id)
    return(extract_all)