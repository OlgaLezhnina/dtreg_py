from .dtr_interface import supply_dtr_with_info
from types import SimpleNamespace

def load_datatype(template_doi):
    datypreg, templ_info = supply_dtr_with_info(template_doi)
    result_dict = write_objects(templ_info)
    result = SimpleNamespace(**result_dict)
    return result

def write_objects(templ_info):
    objects = {}
    for key in templ_info.keys():
        dt_name = templ_info[key][0][0]["dt_name"]
        prop_list = [] 
        if len(templ_info[key][1]) != 0:
            for props in templ_info[key][1]:
                prop_list.append(props["dtp_name"]) 
        def __init__(self, *args, **kwargs):
            for dtp_name in self.prop_list:
                setattr(self, dtp_name, kwargs.get(dtp_name))                
        class_object = type(dt_name, 
                 (),                    
                 {"dt_name": dt_name, 
                  "dt_id": templ_info[key][0][0]["dt_id"] ,
                  "dt_class": templ_info[key][0][0]["dt_class"],
                  "prop_list":prop_list,
                  "__init__": __init__}) 
        objects.update({dt_name: class_object})
    return objects
    