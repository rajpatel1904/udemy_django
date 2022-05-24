import re
from winreg import REG_QWORD
from django.shortcuts import render

# Create your views here.

def example_view(request):
    return render(request,'my_app/example.html')

def variable_view(request):
    my_var={
        'first_name':'Raj',
        'last_name':'Patel',
        'some_list':[1,2,3,4],
        'some_dict':{'inside_key':'inside_value'},
    }
    return render(request,'my_app/variable.html',context=my_var)



