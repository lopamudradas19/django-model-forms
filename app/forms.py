from django import forms
from app.models import *
# from app.forms import *
class TopicModelForm(forms.ModelForm):
    class Meta():
        model=Topic
        fields='__all__'
        wedgets={'topic_name':forms.RadioSelect}
        help_texts={'topic_name':'select required data'}

class WebpageModelForm(forms.ModelForm):
    class Meta():
        model=Webpage
        fields='__all__'
        wedgets={'topic_name':forms.RadioSelect}
        help_texts={'topic_name':'select required data'}
        labels={'topic_name':'TN'}


class AccessRecordModelForm(forms.ModelForm):
    class Meta():
        model=AccessRecord
        fields='__all__'
        wedgets={'topic_name':forms.RadioSelect}
        help_texts={'name':'select required data'}
        labels={'name':'NAME'}

