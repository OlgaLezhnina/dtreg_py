from typing import Protocol
from .extract_epic import extract_epic
from .extract_orkg import extract_orkg
from .from_static import from_static

class DataTypeReg(Protocol):
    def get_template_info(self, template_doi):
        pass

class Epic:
    def get_template_info(self, template_doi):
        static = from_static(template_doi)
        if static is None:
           template_info = extract_epic(template_doi)
        else:
           template_info = static
        return template_info       

class Orkg:
    def get_template_info(self, template_doi):
        static = from_static(template_doi)
        if static is None:
           template_info = extract_orkg(template_doi)
        else:
           template_info = static
        return template_info             

def select_dtr(template_doi):
    datypreg = None
    if template_doi.split("/", 4)[3] == '21.T11969':
        datypreg = Epic()
    elif "orkg.org" in template_doi.split("/", 4)[2]:
        datypreg = Orkg()
    else:
        print("Please check whether the schema belongs to the ePIC or the ORKG dtr")        
    return datypreg

def supply_dtr_with_info(template_doi):
    dtr = select_dtr(template_doi)
    template_info = dtr.get_template_info(template_doi)
    return dtr, template_info 
    