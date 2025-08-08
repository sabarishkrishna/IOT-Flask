import json

def get_config(key):
    config_file = "/Users/sabarish/Desktop/flask/config.json"
    file = open(config_file, "r")
    config = json.loads(file.read())
    file.close()
    
    if key in config:
        return config[key]
    else:
        raise Exception("Key {} has not been identified.".format(key))
    

