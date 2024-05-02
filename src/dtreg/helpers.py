def format_string(text):
  return text.lower().replace(" ", "_").replace("-", "_")

def generate_uid():
    i = 0
    def function():
        nonlocal i
        i += 1
        return i
    return function 