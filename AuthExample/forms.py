from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from .models import * 
from django.db import transaction
from django.forms import ModelForm, ModelChoiceField

class StudentSignupform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username','password1','password2','cohort']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False) # save the details but dont put in database
        user.is_student = True
        print(user)
        user.save()
        return user


class TeacherSignupform(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False) # save the details but dont put in database
        user.is_student = False
        user.save()
        return user
    
#TEACHER ROLE
class TeacherBookingForm(ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField()
    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'end_time','class_types', 'room','module', 'cohort']


# cleaned_data validated form input fields and their values.
    def clean(self):
        end_time = self.cleaned_data['end_time']
        date = self.cleaned_data['date']
        room = self.cleaned_data['room']
        start_time = self.cleaned_data['start_time']


        if date < timezone.now().date():
            raise forms.ValidationError(message='Date cannot be in the past')

        
        bookings = Booking.objects.filter(date=date, room=room)
        
        for booking in bookings:
            if start_time >= end_time:
                raise forms.ValidationError('Start Time must be before End Time')

    # Check if there is any overlap between the new booking and existing ones
            if not (end_time <= booking.start_time or start_time >= booking.end_time):
                raise forms.ValidationError('This time slot is already booked')
                
        return self.cleaned_data
    
class StudentBookingForm(ModelForm):
    date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField()

    class Meta:
        model = Booking
        fields = ['date', 'start_time', 'end_time','activity_types', 'room', 'cohort', 'module']


# cleaned_data validated form input fields and their values.
    def clean(self):
        end_time = self.cleaned_data['end_time']
        date = self.cleaned_data['date']
        room = self.cleaned_data['room']
        start_time = self.cleaned_data['start_time']


        if date < timezone.now().date():
            raise forms.ValidationError(message='Date cannot be in the past')

        
        bookings = Booking.objects.filter(date=date, room=room)
        
        for booking in bookings:
            if start_time >= end_time:
                raise forms.ValidationError('Start Time must be before End Time')

    # Check if there is any overlap between the new booking and existing ones
            if not (end_time <= booking.start_time or start_time >= booking.end_time):
                raise forms.ValidationError('This time slot is already booked')
                
        return self.cleaned_data