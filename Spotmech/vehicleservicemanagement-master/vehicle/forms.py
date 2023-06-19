from django import forms
from django.contrib.auth.models import User
from . import models
from django.core.validators import MaxValueValidator
from .models import Mechanic, Location

class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']


class MechanicUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }



class MechanicForm(forms.ModelForm):
    latitude = forms.DecimalField(max_digits=9, decimal_places=6, required=False)
    longitude = forms.DecimalField(max_digits=9, decimal_places=6, required=False)

    class Meta:
        model = Mechanic
        fields = ['address', 'mobile', 'profile_pic', 'skill']

    def save(self, commit=True):
        mechanic = super(MechanicForm, self).save(commit=False)
        if commit:
            mechanic.save()

        latitude = self.cleaned_data.get('latitude')
        longitude = self.cleaned_data.get('longitude')

        if latitude and longitude:
            location = Location.objects.create(latitude=latitude, longitude=longitude)
            mechanic.location = location
            mechanic.save()

        return mechanic


class MechanicRatingForm(forms.Form):
    rating=forms.DecimalField(
        decimal_places=2,
        max_digits=5,
        validators=[MaxValueValidator(10)]
    )


class RequestForm(forms.ModelForm):
    class Meta:
        model=models.Request
        fields=['category','vehicle_no','vehicle_name','vehicle_model','vehicle_brand','problem_description']
        widgets = {
        'problem_description':forms.Textarea(attrs={'rows': 3, 'cols': 30})
        }

class AdminRequestForm(forms.Form):
    #to_field_name value will be stored when form is submitted.....__str__ method of customer model will be shown there in html
    customer=forms.ModelChoiceField(queryset=models.Customer.objects.all(),empty_label="Customer Name",to_field_name='id')
    mechanic=forms.ModelChoiceField(queryset=models.Mechanic.objects.all(),empty_label="Mechanic Name",to_field_name='id')
    cost=forms.IntegerField()

class AdminApproveRequestForm(forms.Form):
    mechanic=forms.ModelChoiceField(queryset=models.Mechanic.objects.all(),empty_label="Mechanic Name",to_field_name='id')
    cost=forms.IntegerField()
    stat=(('Pending','Pending'),('Approved','Approved'),('Released','Released'))
    status=forms.ChoiceField( choices=stat)


class UpdateCostForm(forms.Form):
    cost=forms.IntegerField()

class MechanicUpdateStatusForm(forms.Form):
    stat=(('Approved','Approved'),('Repairing','Repairing'),('Repairing Done','Repairing Done'))
    status=forms.ChoiceField( choices=stat)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model=models.Feedback
        fields=['by','message']
        widgets = {
        'message':forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }

#for Attendance related form
presence_choices=(('Present','Present'),('Absent','Absent'))
class AttendanceForm(forms.Form):
    present_status=forms.ChoiceField( choices=presence_choices)
    date=forms.DateField()

class AskDateForm(forms.Form):
    date=forms.DateField()


#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
