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
    def add_context(self, prefix):
        context_info = {
            "doi": prefix}
        return context_info  
    def add_dt_type(self, identifier):
        dt_type = "doi:" + identifier
        return dt_type  

class Orkg:
    def get_template_info(self, template_doi):
        template_info = extract_orkg(template_doi)
        return template_info
    def add_context(self, prefix):
        context_info = {
            "orkgr": prefix + "resource/",
            "orkgp": prefix + "property/"}
        return context_info  
    def add_dt_type(self, identifier):
        dt_type = "orkgr:" + identifier
        return dt_type
      

def select_dtr(template_doi):
    datypreg = None
    if template_doi.split("/", 4)[3] == '21.T11969':
        datypreg = Epic
    elif "orkg.org" in template_doi.split("/", 4)[2]:
        datypreg = Orkg
    else:
        print("Please check whether the schema belongs to the ePIC or the ORKG dtr")        
    return datypreg


    