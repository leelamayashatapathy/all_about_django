# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student2, Contact, StudentFaker
from django.db.models import Q


def homepage(request):
    # return HttpResponse("It's Homepage Baby")
    if request.method == "POST":
        # for django simple form
        #     data = StudentForm(request.POST)
        #     if data.is_valid():
        #         name = data.cleaned_data['name']
        #         age = data.cleaned_data['age']
        #         phone = data.cleaned_data['phone']
        #         Student2.objects.create(name=name, age=age, phone = phone)
        #         return redirect('/api/thank-you/')
        # else:
        #     print(request.method)

        # context = {'form':StudentForm}
        # return render(request,"index.html",context)

        # for django model form
        form = StudentForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form.save()
            return redirect("/api/thank-you/")
    else:
        form = StudentForm
    context = {"form": form}
    return render(request, "index.html", context)


def contact(request):
    # return HttpResponse("It's Contact Page Baby")

    # context based message
    # names = ['ram','shyam','subham']
    # context = {
    #     'names':names,
    #     'value':1234.00894
    # }
    # context = {'form':StudentForm}
    # return render(request,"contact.html",context)

    # data from html form
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        message = data.get("message")
        Contact.objects.create(name=name, email=email, message=message)

    return render(request, "contact.html")


def service(request):
    return HttpResponse("It's the service page Baby")


def thank_you(request):
    return HttpResponse("Thnk you your data is recorded")


def dynamic(request, email):
    return HttpResponse({"email": email})


# General Search functionality
def search_page(request):
    students = StudentFaker.objects.all()
    search = request.GET.get("search")
    age = request.GET.get('age')
    print(age)
    if search:
        students = StudentFaker.objects.filter(
            Q(name__icontains=search) | Q(email__icontains=search)
         | Q(college__college_name__icontains=search))
        if age == "1":
            students = students.filter(age__gte = 18,age__lte=25)

    context = {"students": students, 'search':search}
    return render(request, "search.html", context)
