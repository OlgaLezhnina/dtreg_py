from typing import Protocol
from .extract_epic import extract_epic
from .extract_orkg import extract_orkg
from .from_static import from_static

def select_dtr(datatype_id):
    selected_class = None
    if datatype_id.split("/", 4)[3] == '21.T11969':
        selected_class = Epic
    elif "orkg.org" in datatype_id.split("/", 4)[2]:
        selected_class = Orkg
    else:
        print("Please check whether the schema belongs to the ePIC or the ORKG dtr")        
    return selected_class

class DataTypeReg(Protocol):
    def get_schema_info(self, datatype_id):
        pass
    def add_context(self, prefix):
        pass
    def add_dt_type(self, identifier):
        pass
    def add_dtp_type(self, identifier):
        pass
    def add_df_constants(self):
        pass

class Epic:
    def get_schema_info(self, datatype_id):
        static = from_static(datatype_id)
        if static is None:
           schema_info = extract_epic(datatype_id)
        else:
           schema_info = static
        return schema_info       
    def add_context(self, prefix):
        context_info = {
            "doi": prefix,
            "columns": prefix + "0424f6e7026fa4bc2c4a#columns",
            "col_number":  prefix + "65ba00e95e60fb8971e6#number",
            "col_titles":  prefix + "65ba00e95e60fb8971e6#titles",
            "rows":  prefix + "0424f6e7026fa4bc2c4a#rows",
            "row_number":  prefix + "9bf7a8e8909bfd491b38#number",
            "row_titles":  prefix + "9bf7a8e8909bfd491b38#titles",
            "cells":  prefix + "9bf7a8e8909bfd491b38#cells",
            "column":  prefix + "4607bc7c42ac8db29bfc#column",
            "value":  prefix + "4607bc7c42ac8db29bfc#value"}
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
            "column": "doi:65ba00e95e60fb8971e6",            
            "row": "doi:9bf7a8e8909bfd491b38",
            "cell": "doi:4607bc7c42ac8db29bfc"}
        return df_constants

class Orkg:
    def get_schema_info(self, datatype_id):
        schema_info = extract_orkg(datatype_id)
        return schema_info
    def add_context(self, prefix):
        context_info = {
            "orkgc": prefix + "class/",
            "orkgr": prefix + "resource/",
            "orkgp": prefix + "property/",
            "columns": prefix + "property/" + "CSVW_Columns",
            "col_number": prefix + "property/" + "CSVW_Number",
            "col_titles": prefix + "property/" + "CSVW_Titles",
            "rows": prefix + "property/" + "CSVW_Rows",
            "row_number": prefix + "property/" + "CSVW_Number",
            "row_titles": prefix + "property/" + "CSVW_Titles",
            "cells": prefix + "property/" + "CSVW_Cells",
            "column": prefix + "property/" + "CSVW_Column",
            "value": prefix + "property/" + "CSVW_Value",
            "label": "http://www.w3.org/2000/01/rdf-schema#label"}
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
            "column": "orkgc:Column",
            "row": "orkgc:Row",
            "cell": "orkgc:Cell"}
        return df_constants    