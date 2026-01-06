
from django.contrib import admin
from django.urls import path
from myapp.views import Create_Student,Student_List,Edit_Student,Delete_Student,Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',Home,name='Home'),
    path('createstudent/',Create_Student,name='Create_Student'),
    path('studentlist/',Student_List,name='Student_List'),
    path('editstudent/<int:id>/',Edit_Student,name='Edit_Student'),
    path('deletestudent/<int:id>/',Delete_Student,name='Delete_Student'),
]
