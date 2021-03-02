from django.form import ModelForm
from .models import Question, Choice

class PollForm(ModelForm):
    class meta:
        model = Question
        fields = '__all__'