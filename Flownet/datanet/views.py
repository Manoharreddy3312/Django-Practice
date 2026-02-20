from django.shortcuts import render

import datanet

students=[
    {'name':'Priya','phone':9848687932,'mail':'dadlittleprincess@gmail.com','clg':"HITS","stream":"CSE",'branch':'CS',"gender":'female','percentage':'85%','yop':2025,'dob':"20-9-1947",'address':'KPHB','attendance':35},

    {'name':'Sagar','phone':9848687933,'mail':'sagar@gmail.com','clg':"HITS","stream":"CSE",'branch':'CS',"gender":'male','percentage':'80%','yop':2025,'dob':"20-9-1947",'address':'KPHB','attendance':30},

    {'name':'Yashwanth','phone':9848687973,'mail':'yashwanth@gmail.com','clg':"NIT","stream":"CSE",'branch':'CS',"gender":'male','percentage':'70%','yop':2024,'dob':"20-9-1948",'address':'Addagutta','attendance':70},
]

emp = [
    {
        'name' : "Manohar",'id': 1,'dob':'20-02-2000','doj':'20-02-2020','address':'Hyderabad','blood_group':'B+','role':'Software Engineer','sal':50000,'gender':'male',
    },

    {
        'name' : "Priya",'id': 2,'dob':'20-02-2000','doj':'20-02-2020','address':'Hyderabad','blood_group':'B+','role':'Software Engineer','sal':50000,'gender':'female',
    }
,
    {
        'name' : "Rajesh",'id': 3,'dob':'15-05-2001','doj':'10-06-2021','address':'Bangalore','blood_group':'O+','role':'Senior Developer','sal':65000,'gender':'male',
    },
    {
        'name' : "Anjali",'id': 4,'dob':'22-08-1999','doj':'15-07-2020','address':'Chennai','blood_group':'A+','role':'QA Engineer','sal':45000,'gender':'female',
    },
    {
        'name' : "Vikram",'id': 5,'dob':'10-12-2000','doj':'20-01-2021','address':'Mumbai','blood_group':'B-','role':'DevOps Engineer','sal':70000,'gender':'male',
    },
    {
        'name' : "Deepa",'id': 6,'dob':'05-03-2002','doj':'12-08-2022','address':'Pune','blood_group':'O-','role':'Data Analyst','sal':55000,'gender':'female',
    },
    {
        'name' : "Arjun",'id': 7,'dob':'18-07-2001','doj':'25-09-2021','address':'Hyderabad','blood_group':'AB+','role':'Frontend Developer','sal':60000,'gender':'male',
    },
    {
        'name' : "Neha",'id': 8,'dob':'30-11-1998','doj':'08-02-2020','address':'Delhi','blood_group':'B+','role':'Backend Developer','sal':62000,'gender':'female',
    },
    {
        'name' : "Rohan",'id': 9,'dob':'12-04-2000','doj':'16-05-2021','address':'Bengaluru','blood_group':'A-','role':'ML Engineer','sal':75000,'gender':'male',
    },
    {
        'name' : "Pooja",'id': 10,'dob':'28-09-2001','doj':'10-10-2022','address':'Hyderabad','blood_group':'O+','role':'Tech Lead','sal':80000,'gender':'female',
    },
    {
        'name' : "Aditya",'id': 11,'dob':'14-06-2000','doj':'20-07-2021','address':'Bangalore','blood_group':'B+','role':'Software Engineer','sal':50000,'gender':'male',
    },
    {
        'name' : "Riya",'id': 12,'dob':'07-02-1999','doj':'15-03-2020','address':'Mumbai','blood_group':'A+','role':'UI Designer','sal':48000,'gender':'female',
    },
    {
        'name' : "Karthik",'id': 13,'dob':'21-08-2001','doj':'30-09-2022','address':'Chennai','blood_group':'AB-','role':'Cloud Engineer','sal':72000,'gender':'male',
    },
    {
        'name' : "Swati",'id': 14,'dob':'11-01-2000','doj':'05-02-2021','address':'Pune','blood_group':'O-','role':'QA Lead','sal':58000,'gender':'female',
    },
    {
        'name' : "Nikhil",'id': 15,'dob':'25-05-2002','doj':'12-06-2022','address':'Hyderabad','blood_group':'B-','role':'Junior Developer','sal':40000,'gender':'male',
    },
    {
        'name' : "Divya",'id': 16,'dob':'19-12-1998','doj':'22-01-2020','address':'Bengaluru','blood_group':'A+','role':'Database Admin','sal':60000,'gender':'female',
    },
    {
        'name' : "Suresh",'id': 17,'dob':'03-10-2000','doj':'09-11-2021','address':'Delhi','blood_group':'O+','role':'Systems Engineer','sal':55000,'gender':'male',
    },
    {
        'name' : "Isha",'id': 18,'dob':'16-04-1999','doj':'18-05-2020','address':'Mumbai','blood_group':'AB+','role':'Product Manager','sal':85000,'gender':'female',
    },
    {
        'name' : "Rahul",'id': 19,'dob':'29-07-2001','doj':'14-08-2022','address':'Bangalore','blood_group':'B+','role':'Security Engineer','sal':68000,'gender':'male',
    },
    {
        'name' : "Megha",'id': 20,'dob':'08-11-2000','doj':'20-12-2021','address':'Chennai','blood_group':'O-','role':'Business Analyst','sal':56000,'gender':'female',
    },
    {
        'name' : "Pranav",'id': 21,'dob':'13-03-2002','doj':'25-04-2022','address':'Hyderabad','blood_group':'A-','role':'Support Engineer','sal':38000,'gender':'male',
    },
    {
        'name' : "Kavya",'id': 22,'dob':'27-06-1999','doj':'30-07-2020','address':'Pune','blood_group':'B-','role':'Content Writer','sal':42000,'gender':'female',
    },
    {
        'name' : "Ashok",'id': 23,'dob':'09-09-2000','doj':'15-10-2021','address':'Bengaluru','blood_group':'AB+','role':'Network Engineer','sal':63000,'gender':'male',
    },
    {
        'name' : "Priyanka",'id': 24,'dob':'22-05-2001','doj':'08-06-2022','address':'Delhi','blood_group':'O+','role':'HR Manager','sal':70000,'gender':'female',
    },
    {
        'name' : "Varun",'id': 25,'dob':'05-01-2000','doj':'10-02-2021','address':'Mumbai','blood_group':'B+','role':'Infrastructure Lead','sal':78000,'gender':'male',
    },
    {
        'name' : "Ananya",'id': 26,'dob':'31-08-1999','doj':'12-09-2020','address':'Bangalore','blood_group':'A+','role':'Scrum Master','sal':65000,'gender':'female',
    },
    {
        'name' : "Sanjay",'id': 27,'dob':'17-04-2001','doj':'22-05-2022','address':'Chennai','blood_group':'O-','role':'Architect','sal':90000,'gender':'male',
    },
    {
        'name': "Nisha",'id': 28,'dob':'14-10-2000','doj':'18-11-2021','address':'Hyderabad','blood_group':'B-','role':'Quality Assurance','sal':50000,'gender':'female',
    },
    {
        'name' : "Michael",'id': 29,'dob':'02-07-1998','doj':'05-08-2019','address':'Pune','blood_group':'AB-','role':'Solutions Architect','sal':95000,'gender':'male',
    },
    {
        'name' : "Sophia",'id': 30,'dob':'20-11-2001','doj':'15-12-2022','address':'Bengaluru','blood_group':'A-','role':'Application Support','sal':43000,'gender':'female',
    },
    {
        'name' : "David",'id': 31,'dob':'11-02-2000','doj':'20-03-2021','address':'Delhi','blood_group':'B+','role':'IT Manager','sal':82000,'gender':'male',
    },
    {
        'name' : "Emma",'id': 32,'dob':'25-06-1999','doj':'10-07-2020','address':'Mumbai','blood_group':'O+','role':'Release Manager','sal':72000,'gender':'female',
    },
    {
        'name' : "James",'id': 33,'dob':'08-12-2001','doj':'30-01-2023','address':'Bangalore','blood_group':'A+','role':'Intern Developer','sal':25000,'gender':'male',
    },
    {
        'name' : "Olivia",'id': 34,'dob':'19-09-2000','doj':'24-10-2021','address':'Chennai','blood_group':'AB+','role':'Compliance Officer','sal':60000,'gender':'female',
    },
    {
        'name' : "Robert",'id': 35,'dob':'04-05-1998','doj':'08-06-2019','address':'Hyderabad','blood_group':'O-','role':'Principal Engineer','sal':100000,'gender':'male',
    },
    {
        'name' : "Isabella",'id': 36,'dob':'16-03-2002','doj':'20-04-2022','address':'Pune','blood_group':'B-','role':'Documentation Lead','sal':52000,'gender':'female',
    },
    {
        'name' : "William",'id': 37,'dob':'12-11-2000','doj':'16-12-2021','address':'Bengaluru','blood_group':'A-','role':'Technical Writer','sal':48000,'gender':'male',
    },
    {
        'name' : "Charlotte",'id': 38,'dob':'28-07-1999','doj':'02-08-2020','address':'Delhi','blood_group':'B+','role':'Finance Manager','sal':75000,'gender':'female',
    },
    {
        'name' : "Benjamin",'id': 39,'dob':'10-04-2001','doj':'15-05-2022','address':'Mumbai','blood_group':'O+','role':'Operations Lead','sal':70000,'gender':'male',
    },
    {
        'name' : "Amelia",'id': 40,'dob':'23-01-2000','doj':'28-02-2021','address':'Bangalore','blood_group':'AB+','role':'Recruiter','sal':55000,'gender':'female',
    },
    {
        'name' : "Lucas",'id': 41,'dob':'07-08-2002','doj':'10-09-2022','address':'Chennai','blood_group':'A+','role':'Trainee Engineer','sal':30000,'gender':'male',
    },
    {
        'name' : "Harper",'id': 42,'dob':'30-05-1998','doj':'04-06-2019','address':'Hyderabad','blood_group':'O-','role':'Audit Manager','sal':68000,'gender':'female',
    },
    {
        'name' : "Alexander",'id': 43,'dob':'14-09-2000','doj':'20-10-2021','address':'Pune','blood_group':'B-','role':'Performance Lead','sal':76000,'gender':'male',
    },
    {
        'name' : "Mia",'id': 44,'dob':'06-02-1999','doj':'12-03-2020','address':'Bengaluru','blood_group':'A-','role':'Sales Executive','sal':58000,'gender':'female',
    },
    {
        'name' : "Mason",'id': 45,'dob':'21-06-2001','doj':'25-07-2022','address':'Delhi','blood_group':'B+','role':'Support Lead','sal':62000,'gender':'male',
    },
    {
        'name' : "Evelyn",'id': 46,'dob':'13-10-2000','doj':'18-11-2021','address':'Mumbai','blood_group':'O+','role':'Vendor Manager','sal':61000,'gender':'female',
    },
    {
        'name' : "Logan",'id': 47,'dob':'09-03-2002','doj':'12-04-2022','address':'Bangalore','blood_group':'AB-','role':'Junior Analyst','sal':35000,'gender':'male',
    },
    {
        'name' : "Grace",'id': 48,'dob':'24-11-1999','doj':'28-12-2020','address':'Chennai','blood_group':'A+','role':'Senior QA','sal':64000,'gender':'female',
    }

]

# Create your views here.
def student(request):
   
    context = {
       
        'data':students

    }

    return render(request,"table.html",context)


def employee(request):
    context ={
        'company':'Google',
        'data' : emp
    }

    return render(request,'employee.html',context)