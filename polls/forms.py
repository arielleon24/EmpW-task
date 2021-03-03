from django import forms
from .models import Question, Choice

class PollForm(forms.ModelForm):
    class meta:
        model = Question
        fields = [
            'question_text',
            'choices'
        ]