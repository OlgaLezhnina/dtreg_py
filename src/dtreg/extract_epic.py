#from .request_epic import request_epic

def extract_epic(template_doi):
    extract_all = {}
    def extractor_function(template_doi):
        info = request_epic(template_doi)
        schema_dict = {
            "name": info["name"],
            "identifier": info["Identifier"],
            "schema_type": info["Schema"]["Type"]}
        extracted = [[schema_dict]]
        all_props = []
        for prop in info["Schema"].get("Properties", []):
            if "Type" in prop:
                specific_prop_dict = {
                    "prop_name": prop["Name"],
                    "type_id": prop["Type"],
                    "cardinality": prop["Properties"]["Cardinality"],
                    "nested": True}
                extractor_function("https://doi.org/" + prop["Type"])
            else:        
                specific_prop_dict = {
                    "prop_name": prop["Property"],
                    "type_id": "value",
                    "cardinality": "no_info",
                    "nested": False}   
            all_props.append(specific_prop_dict)
        extracted.append(all_props)
        extract_all[schema_dict["name"]] = list(extracted) 
        return(extract_all)
    extractor_function(template_doi)
    return(extract_all)