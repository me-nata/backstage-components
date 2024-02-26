import os


TEMPLATES_FOLDER = os.path.join(os.path.dirname(__file__), 'jinja')

TEMPLATES_PATH = {
    "api":       os.path.join("api.j2"),
    "base":      os.path.join("base.j2"),
    "component": os.path.join("component.j2"),
    "domain":    os.path.join("domain.j2"),
    "group":     os.path.join("group.j2"),
    "location":  os.path.join("location.j2"),
    "resource":  os.path.join("resource.j2"),
    "system":    os.path.join("system.j2"),
    "user":      os.path.join("user.j2")
}