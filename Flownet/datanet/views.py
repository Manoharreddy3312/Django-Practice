from django.shortcuts import render

import datanet

students=[
    {'name':'Priya','phone':9848687932,'mail':'dadlittleprincess@gmail.com','clg':"HITS","stream":"CSE",'branch':'CS',"gender":'female','percentage':'85%','yop':2025,'dob':"20-9-1947",'address':'KPHB','attendance':35},

    {'name':'Sagar','phone':9848687933,'mail':'sagar@gmail.com','clg':"HITS","stream":"CSE",'branch':'CS',"gender":'male','percentage':'80%','yop':2025,'dob':"20-9-1947",'address':'KPHB','attendance':30},

    {'name':'Yashwanth','phone':9848687973,'mail':'yashwanth@gmail.com','clg':"NIT","stream":"CSE",'branch':'CS',"gender":'male','percentage':'70%','yop':2024,'dob':"20-9-1948",'address':'Addagutta','attendance':70},


    
    
]


# Create your views here.
def student(request):
   
    context = {
       
        'data':students

    }

    return render(request,"table.html",context)