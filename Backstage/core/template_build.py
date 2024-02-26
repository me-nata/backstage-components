import re


class TemplateBuilder:
    def render_template(self, template_loaded, template_data: dict):
        rendered_yaml = template_loaded.render(template_data)
        return self.pos_processing(rendered_yaml)
    
    def pos_processing(self, rendered_yaml):
        return re.sub(r'\n\s*\n', '\n', rendered_yaml)

    def save_template(self, outfile_path, template_obj):
        with open(outfile_path, 'w') as file:
            file.write(template_obj)
