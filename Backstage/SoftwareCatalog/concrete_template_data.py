from ..core.template_data import TemplateData


#*******************************************************
# Metadados (comum a todos)
#*******************************************************

class SoftwareCatalogTemplateData(TemplateData):
    def __init__(self, entity_model) -> None:
        metadata_model = {
            'name': '',
            'namespace': None,
            'title': None,
            'description': None,
            'labels': None,
            'annotations': None,
            'tags': None,
            'links': None,
        }
        entity_model.update(metadata_model)
        super().__init__(entity_model)

#*******************************************************
# Profile
#*******************************************************
class Profile(TemplateData):
    def __init__(self) -> None:
        super().__init__({
            'displayName': '',
            'email': '',
            'picture': ''
        })


#*******************************************************
# Entity Api
#*******************************************************
class Api(SoftwareCatalogTemplateData):
    def __init__(self) -> None:
        super().__init__({
            'type': '',
            'lifecycle': '',
            'owner': '',
            'system': None,
            'definition': ''
        })

#*******************************************************
# Entity Component
#*******************************************************
class Component(TemplateData):
    def __init__(self) -> None:
        super().__init__({
            'type': '',
            'lifecycle': '',
            'owner': '',
            'system': None,
            'subcomponentOf': None,
            'providesApis': None,
            'consumesApis': None,
            'dependsOn': None
        })

#*******************************************************
# Entity Group
#*******************************************************
class Group(TemplateData):
    def __init__(self) -> None:
        super().__init__({
            'type': '',
            'profile': None,
            'parent': None,
            'children': '',
            'members': None,
        })

#*******************************************************
# Entity User
#*******************************************************
class User(TemplateData):
    def __init__(self) -> None:
        super().__init__({
            'profile': None,
            'memberOf': None,
            'children': '',
            'members': None,
        })

#*******************************************************
# Entity Resource
#*******************************************************
class Resource(TemplateData):
    def __init__(self) -> None:
        super().__init__({
            'owner': '',
            'type': '',
            'system': None,
            'dependsOn': None,
            'dependencyOf': None,
        })

#*******************************************************
# Entity System
#*******************************************************
class System(TemplateData):
    def __init__(self) -> None:
        super().__init__({
            'owner': '',
            'domain': '',
        })

#*******************************************************
# Entity Domain
#*******************************************************
class Domain(TemplateData):
    def __init__(self) -> None:
        super().__init__({
            'owner': '',
        })

#*******************************************************
# Entity Location
#*******************************************************
class Location(TemplateData):
    def __init__(self) -> None:
        super().__init__({
            'type': None,
            'target': None,
            'targets': None,
            'presence': None,
        })