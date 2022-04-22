from django import forms
from web.models import Feedback, Vacancy


class FeedbackForm(forms.ModelForm):
    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'rows': '2'})
    )

    def clean_email(self):
        email = self.cleaned_data['email']
        domain = email.split('.')[-1]
        if domain in ['com', 'net', 'org', 'xyz', 'de', 'fr', 'ua', 'nl', 'cz', 'group', 'biz']:
            raise forms.ValidationError(f'Использование почтового ящика в домене .{domain} заблокированно')
        return email

    class Meta:
        model = Feedback
        fields = ('name', 'phone', 'email', 'text', 'site')


class VacancyForm(forms.ModelForm):

    class Meta:
        model = Vacancy
        fields = ('name', 'lastname', 'email', 'phone', 'portfolio', 'profile', 'where', 'resume', 'letter')

