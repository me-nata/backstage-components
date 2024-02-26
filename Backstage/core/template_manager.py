from .template_build import TemplateBuilder
from .template_loader import TemplateLoader


class TemplateManager:
    def __init__(self, env) -> None:
        self.builder = TemplateBuilder()
        self.loader = TemplateLoader(env)

    def match(self, instance_template_data, save=''):
        loader = self.loader.get(instance_template_data.type)
        rendered = self.builder.render_template(
            loader,
            instance_template_data.data
        )

        if save != '':
            with open(save, 'w') as file:
                file.write(rendered)
                file.close()

        return rendered
    
    def stack(self, *args, save=''):
        rendered = '---\n'
        for instance in args:
            rendered += self.match(instance)
            rendered += '\n---\n'

        if save != '':
            with open(save, 'w') as file:
                file.write(rendered)
                file.close()

        return rendered
