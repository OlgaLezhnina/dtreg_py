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
    def add_dtp_type(self, identifier):
        dtp_type = "doi:" + identifier
        return dtp_type
    def add_df_constants(self):
        df_constants = {
            "table": "doi:0424f6e7026fa4bc2c4a",
            "columns_p": "doi:0424f6e7026fa4bc2c4a#columns",
            "column": "doi:65ba00e95e60fb8971e6",
            "col_number_p": "doi:65ba00e95e60fb8971e6#number",
            "col_titles_p": "doi:65ba00e95e60fb8971e6#titles",
            "rows_p": "doi:0424f6e7026fa4bc2c4a#rows",
            "row": "doi:9bf7a8e8909bfd491b38",
            "row_number_p": "doi:9bf7a8e8909bfd491b38#number",
            "row_titles_p": "doi:9bf7a8e8909bfd491b38#titles",
            "cells_p": "doi:9bf7a8e8909bfd491b38#cells",
            "cell": "doi:4607bc7c42ac8db29bfc",
            "column_p": "doi:4607bc7c42ac8db29bfc#column",
            "value_p": "doi:4607bc7c42ac8db29bfc#value"}
        return df_constants

class Orkg:
    def get_template_info(self, template_doi):
        template_info = extract_orkg(template_doi)
        return template_info
    def add_context(self, prefix):
        context_info = {
            "orkgc": prefix + "class/",
            "orkgr": prefix + "resource/",
            "orkgp": prefix + "property/"}
        return context_info  
    def add_dt_type(self, identifier):
        dt_type = "orkgr:" + identifier
        return dt_type
    def add_dtp_type(self, identifier):
        dtp_type = "orkgp:" + identifier
        return dtp_type
    def add_df_constants(self):
        df_constants = {
            "table": "orkgc:Table",
            "columns_p": "orkgp:CSVW_Columns",
            "column": "orkgc:Column",
            "col_number_p": "orkgp:CSVW_Number",
            "col_titles_p": "orkgp:CSVW_Titles",
            "rows_p": "orkgp:CSVW_Rows",
            "row": "orkgc:Row",
            "row_number_p": "orkgp:CSVW_Number",
            "row_titles_p": "orkgp:CSVW_Titles",
            "cells_p": "orkgp:CSVW_Cells",
            "cell": "orkgc:Cell",
            "column_p": "orkgp:CSVW_Column",
            "value_p": "orkgp:CSVW_Value"}
        return df_constants
      

def select_dtr(template_doi):
    datypreg = None
    if template_doi.split("/", 4)[3] == '21.T11969':
        datypreg = Epic
    elif "orkg.org" in template_doi.split("/", 4)[2]:
        datypreg = Orkg
    else:
        print("Please check whether the schema belongs to the ePIC or the ORKG dtr")        
    return datypreg


    