from django.urls import path
from admissions.views import addAdmissions
from admissions.views import admissionsReport
from admissions.views import addVendor
from admissions.views import deleteStudent
from admissions.views import updateStudent

urlpatterns = [
    path('newadm/', addAdmissions),
    path('admreport/', admissionsReport),
    path('newvendor/',addVendor),
    path('delete/<int:id>',deleteStudent),
    path('update/<int:id>',updateStudent),
]