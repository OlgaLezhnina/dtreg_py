from .request_dtr import request_dtr

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
            if "Type" in prop:
                specific_prop_dict = {
                    "dtp_name": prop["Name"],
                    "dtp_id": info["name"] + "#" + prop["Name"],
                    "dtp_cardinality": prop["Properties"]["Cardinality"],
                    "dtp_value_class": prop["Type"],
                    "nested": True}
                extractor_function("https://doi.org/" + prop["Type"])
            else:        
                specific_prop_dict = {
                    "dtp_name": prop["Property"],
                    "dtp_id": info["name"] + "#" + prop["Property"],
                    "dtp_cardinality": "no_info",
                    "dtp_value_class": prop["Value"],
                    "nested": False}   
            all_props.append(specific_prop_dict)
        extracted.append(all_props)
        extract_all[schema_dict["dt_name"]] = list(extracted) 
        return(extract_all)
    extractor_function(dt_id)
    return(extract_all)