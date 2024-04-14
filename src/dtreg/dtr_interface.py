from typing import Protocol
from .extract_epic import extract_epic
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
      
def select_dtr(template_doi):
    if template_doi.split("/", 4)[3] == '21.T11969':
        datypreg = Epic()
        return datypreg

def supply_dtr_with_info(template_doi):
    dtr = select_dtr(template_doi)
    template_info = dtr.get_template_info(template_doi)
    return dtr, template_info 
    