from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django.views.generic import CreateView
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def index(request):
        user = request.user
        if user.is_anonymous: 
            #if user isnt logged in  
            return render(request, 'index.html')
        
        elif user.is_student:
                # user is student
            return render(request, 'student_dashboard.html')
        elif not user.is_student:
            # user is teachet 
            return render(request, 'teacher_dashboard.html')
        else:
            # not logged in at all 
            # either show generic landing page 
            # or redirect to login 
            return render(request, 'index.html')


def logout_user(request):
    logout(request)
    return redirect("/")

# Create your views here.
class StudentSignupView(CreateView):
    model = User
    form_class = StudentSignupform
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


class TeacherSignupView(CreateView):
    model = User
    form_class = TeacherSignupform
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')
    
#TEACHER BOOKING
@login_required
def teacher_booking(request):
    user = request.user
    if request.method == 'POST':
        # the user has pressed "submit" and is sending us data to store
        form = TeacherBookingForm(request.POST)
        if form.is_valid():
            # if the form is valid
            booking = form.save(commit=False)
            booking.user_id = user
            booking.save()
            return redirect('/teachertimetable')# does not exist yet
        else:
            return render(request, 'teacher_booking.html', {'form': form})
    else:
        # if the user is trying to view the form
        form = TeacherBookingForm()
        return render(request, 'teacher_booking.html', {'form': form})


@login_required
def teacher_timetable(request):
    user = request.user
    booking = Booking.objects.filter(user_id=user).order_by('date')
    return render(request, 'teacher_booked.html', {'booking':booking})

#STUDENT
@login_required
def student_booking(request):
    user = request.user
    if request.method == 'POST':
        # the user has pressed "submit" and is sending us data to store
        form = StudentBookingForm(request.POST)
        if form.is_valid():
            # if the form is valid
            booking = form.save(commit=False)
            booking.user_id = user
            booking.save()
            return redirect('/studenttimetable')# does not exist yet
        else:
            return render(request, 'student_booking.html', {'form': form})
    else:
        # if the user is trying to view the form
        form = StudentBookingForm()
        return render(request, 'student_booking.html', {'form': form})


@login_required
def student_timetable(request):
    user = request.user
    booking = Booking.objects.filter(user_id=user).order_by('date')
    return render(request, 'student_booked.html', {'booking':booking})