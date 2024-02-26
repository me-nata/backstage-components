from ..core.template_manager import TemplateManager


class SoftwareCatalogManager(TemplateManager):
    def __init__(self) -> None:
        super().__init__('software_catalog')