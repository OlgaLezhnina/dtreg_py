from .dtr_interface import select_dtr
from .helpers import format_string
from .helpers import get_prefix
from types import SimpleNamespace

def load_datatype(template_doi):
    result_dict = write_objects(template_doi)
    result = SimpleNamespace(**result_dict)
    return result

def write_objects(template_doi):
    datypreg = select_dtr(template_doi)
    templ_info = datypreg().get_template_info(template_doi)
    prefix = get_prefix(template_doi)
    objects = {}
    for key in templ_info.keys():
        dt_name = format_string(templ_info[key][0][0]["dt_name"])
        prop_list = [] 
        if len(templ_info[key][1]) != 0:
            for props in templ_info[key][1]:
                prop_list.append(format_string(props["dtp_name"])) 
        def __init__(self, *args, **kwargs):
            for dtp_name in self.prop_list:
                setattr(self, dtp_name, kwargs.get(dtp_name))                
        class_object = type(dt_name, 
                 (datypreg,),                    
                 {"prefix": prefix,
                  "dt_name": dt_name, 
                  "dt_id": templ_info[key][0][0]["dt_id"] ,
                  "dt_class": templ_info[key][0][0]["dt_class"],
                  "prop_list": prop_list,
                  "prop_info": templ_info[key][1],
                  "__init__": __init__}) 
        objects.update({dt_name: class_object})
    return objects
    