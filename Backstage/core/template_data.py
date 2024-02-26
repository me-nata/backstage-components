class InstanceTemplateData:
    def __init__(self, type_template, data) -> None:
        self.type = type_template
        self.data = data

class TemplateData:
    def __init__(self, model: dict = {}) -> None:
        self.model = model

    def new(self, **kargs):
        response = self.model.copy()
        for key, value in kargs.items():
            response[key] = value

        return InstanceTemplateData(
            self.__class__.__name__.lower(), 
            response
        )