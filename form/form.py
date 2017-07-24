from django.forms import ModelForm
from .models import Mform
class A(ModelForm):
    class Meta:
        model=Mform
        fields=['name','article']