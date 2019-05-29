from django import forms
from crudapp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = ("eid", "ename") for only two fields
        fields = "__all__" #for all