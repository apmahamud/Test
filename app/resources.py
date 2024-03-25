from import_export import resources
from .models import Cdr 

class CdrResource(resources.ModelResource):
    class meta:
        model = Cdr
