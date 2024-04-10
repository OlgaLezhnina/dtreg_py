import json
from importlib_resources import files

def from_static(template_id):
    id = template_id.split("/", 3)[3]
    final_template = None
    all_static_data = []
    for f in files("dtreg.data").iterdir():
        text = f.read_text()
        all_static_data.append(text)
    for static in all_static_data:
        if id in static:
            final_template = json.loads(static)
    return final_template