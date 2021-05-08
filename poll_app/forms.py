from django import forms
from poll_app import models
class PollForm(forms.ModelForm):
    class Meta:
        model = models.Poll
        fields = ('question','option_one','option_two','option_three')
    
