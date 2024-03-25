
import re
from django import forms
from app.models import Cdr 

class CdrForm(forms.Form): 
    class meta: 
        model = Cdr
        fields = '__all__'