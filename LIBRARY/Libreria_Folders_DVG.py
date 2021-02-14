import json

def read_json(fullpath):
    """ opens a json and returns it"""
    
    with open(fullpath, "r") as json_file_readed:
        json_readed = json.load(json_file_readed)
    return json_readed



def barr_add(path):
    for x in path:
        path.replace("\\", r"\\")
    print('path:', path)