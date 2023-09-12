from django import forms
from django.forms import ModelForm
from .models import Candidate, GENDER, Email, Chat
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError


class UpperCase(forms.CharField):
    def to_python(self, value):
        return value.upper()


class CandidateRegisterForm(ModelForm):
    job = UpperCase(
        widget=forms.TextInput(attrs={
            'placeholder': 'Example: PD-22',
            'data-mask': 'AA-00'

        })
    )

    class Meta:
        model = Candidate
        fields = '__all__'
        exclude = ['situation']

        widgets = {
            'phone': forms.TextInput(
                attrs={
                    'style': 'font-size: 13px;',
                    'placeholder': 'Phone Number',
                    'data-mask': '(+000) 00-000-000'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'style': 'font-size: 13px;',
                    'placeholder': 'Your Email',
                }
            ),
            'firstname': forms.TextInput(
                attrs={
                    'style': 'font-size: 13px;',
                    'placeholder': 'Your First Name',
                }
            ),
            'lastname': forms.TextInput(
                attrs={
                    'style': 'font-size: 13px;',
                    'placeholder': 'Your Last Name',
                }
            ),


            'gender': forms.RadioSelect(choices=GENDER, attrs={'class': 'btn-check'}),


        }
    exprience = forms.BooleanField(
        label='I have exprience', required=False
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        for obj in Candidate.objects.all():
            if obj.email == email:
                raise forms.ValidationError(
                    'Denied! ' + email + 'is already registered')
        return email

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age < 18 or age > 65:
            raise forms.ValidationError(
                'Denied! Age must be between 18 and 65'
            )
        return age

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if len(phone) != 17:
            raise forms.ValidationError(
                'Denied! The phone field is not complete'
            )
        return phone

    def clean_job(self):
        job = self.cleaned_data.get('job')
        if job == 'PD-22' or job == 'SD-10' or job == 'DA-12':
            return job
        else:
            raise forms.ValidationError(
                'Type for the jobs that are available'
            )


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EmailForm(ModelForm):
    email = forms.EmailField()
    subject = forms.CharField(max_length=50)
    message = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Email
        fields = '__all__'


class ChatForm(ModelForm):
    class Meta:
        model = Chat
        fields = '__all__'
