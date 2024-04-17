from .dtr_interface import supply_dtr_with_info
from types import SimpleNamespace

def load_objects(template_doi):
    datypreg, templ_info = supply_dtr_with_info(template_doi)
    result_dict = write_objects(templ_info)
    result = SimpleNamespace(**result_dict)
    return result

def write_objects(templ_info):
    objects = {}
    for key in templ_info.keys():
        name = templ_info[key][0][0]["name"]
        ObjName = "Obj_" + name
        # get prop names
        prop_list = [] 
        if len(templ_info[key][1]) != 0:
            for props in templ_info[key][1]:
                prop_list.append(props["prop_name"]) 
        def __init__(self, *args, **kwargs):
            for prop_name in prop_list:
                setattr(self, prop_name, kwargs.get(prop_name))                
        ObjName = type(name, 
                 (),                    
                 {"name": name, 
                  "identifier": templ_info[key][0][0]["identifier"] ,
                  "schema_type": templ_info[key][0][0]["schema_type"],
                  "prop_list":prop_list,
                  "__init__": __init__}) 
        objects.update({name: ObjName})
    return objects
    