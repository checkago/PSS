from django import forms

from web.models import Feedback, Vacancy


class FeedbackForm(forms.ModelForm):
    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'rows': '2'})
    )

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'email', 'text')


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ('name', 'lastname', 'email', 'phone', 'portfolio', 'profile', 'where', 'resume', 'letter')