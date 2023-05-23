
import strictyaml as sy
import os
import pathlib

def config_get(
        value: str = None,
        py_config_active:str = "default",
        file:str = 'config.yaml',
        encoding:str = 'utf-8'
    ):
    """Get a value from the config.yaml file."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = pathlib.Path(dir_path, file)
    yaml = open(file, encoding = encoding).read()
    if value == None:
        return sy.load(yaml).data[py_config_active]
    else:
        return sy.load(yaml).data[py_config_active][value]