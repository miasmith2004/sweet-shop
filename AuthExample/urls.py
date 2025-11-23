from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('registerstudent/', views.StudentSignupView.as_view(), name='student_register'),
    path('registerteacher/', views.TeacherSignupView.as_view(), name='register_teacher'),
    path('logout/', views.logout_user, name="logout"),
    path('teacherbooking/', views.teacher_booking, name="teacher_booking"),
    path('teachertimetable/', views.teacher_timetable, name="teacher_timetable"),
    path('studentbooking/', views.student_booking, name="student_booking"),
    path('studenttimetable/', views.student_timetable, name="student_timetable"),
]   


