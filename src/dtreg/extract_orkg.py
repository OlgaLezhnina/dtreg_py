from .request_dtr import request_dtr

def extract_orkg(dt_id):
    extract_all = {}
    def extractor_function(dt_id):
        part = dt_id.split("/", 4)
        orkg_prefix = part[0] + "//" + part[2] + "//api/templates/"
        info = request_dtr(orkg_prefix + part[4])
        schema_dict = {
            "dt_name": info["label"],
            "dt_id": info["id"],
            "dt_class": info["target_class"]["id"]}
        extracted = [[schema_dict]]
        all_props = []
        for prop in info.get("properties", []):
            specific_prop_dict = {
                "dtp_name": prop["path"]["label"],
                "dtp_id": prop["path"]["id"],
                "dtp_card_min": prop["min_count"],
                "dtp_card_max": prop["max_count"]
                }
            if "class" not in prop:
                specific_prop_dict["dtp_value_class"] = prop["datatype"]["id"]
            else:        
                specific_prop_dict["dtp_value_class"] = prop["class"]["id"]
                info_n = request_dtr(orkg_prefix + "?target_class=" + prop["class"]["id"])
                if len(info_n["content"]) > 0:
                   nested_id = info_n["content"][0]["id"]
                   nested_name = info_n["content"][0]["label"]
                   if nested_name not in extract_all:
                       extractor_function(nested_id)
            all_props.append(specific_prop_dict)
        extracted.append(all_props)
        extract_all[schema_dict["dt_name"]] = list(extracted) 
    extractor_function(dt_id)
    return(extract_all)