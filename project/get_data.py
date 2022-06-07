import re
def get_data(path, marker):
    with open (path,'r') as f:
        text = f.read().replace('\n',' ')
        lines = re.split(marker,text)
        lines.pop(0)
        return lines