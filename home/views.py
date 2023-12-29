from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):

    peoples=[
        {'name': 'Chaman Lal', 'age': 23},
        {'name' : 'Abhijeet', 'age': 26},
        {'name' : 'Vicky kausal', 'age': 16},
        {'name' : 'Sandeep', 'age': 29},
        {'name' : 'Yatesh ', 'age' : 24}
    ]

    text="""
num = 1001
temp = num
reverse_num = 0
while temp != 0:
   digit = temp % 10
   reverse_num = (reverse_num * 10) + digit
   temp //= 10
if num == reverse_num:
   print(num, "is a palindrome number")
else:
   print(num, "is not a palindrome number")"""



    return render(request,"index.html", context={'page' : 'Django Tutorial 2023', 'peoples': peoples, 'text': text})


def about(request):
    context = {'page' : 'About'}
    return render(request, "about.html", context)
    

def contact(request):
    context = {'page' : 'Contact'}
    return render(request, "contact.html", context)


def success_page(request):
    print("*" *10)
    return HttpResponse("<h1> Hey this is Succes Page !!</h1>")