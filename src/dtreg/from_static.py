import json
#from pathlib import Path
from importlib_resources import files

def from_static(template_id):
    id = template_id.split("/", 4)[4]
    final_template = None
    for f in files("dtreg.data").iterdir():
        if id in f.stem:            
            file_text = f.read_text()
            final_template = json.loads(file_text)
    return final_template