import yaml
import os
from jinja2 import Environment, FileSystemLoader
from ..templates.dictionary import TEMPLATES_PATH, TEMPLATES_FOLDER


class TemplateLoader:
    def __init__(self, env='') -> None:
        self.template_dictionary = TEMPLATES_PATH
        self.env = Environment(loader=FileSystemLoader(os.path.join(TEMPLATES_FOLDER, env)))
        self.env.filters['to_yaml'] = lambda value: yaml.dump(value, default_flow_style=False)

    def get(self, name_template:str):
        template_path = TEMPLATES_PATH[name_template]
        return self.env.get_template(template_path)