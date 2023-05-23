
import strictyaml as sy
import os
import pathlib

def config_get(
        value: str,
        py_config_active:str = "default",
        file:str = 'config.yaml',
        encoding:str = 'utf-8'
    ):
    """Get a value from the config.yaml file."""
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file = pathlib.Path(dir_path, file)
    yaml = open(file, encoding = encoding).read()
    return sy.load(yaml).data[py_config_active][value]