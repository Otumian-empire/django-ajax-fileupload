from django.shortcuts import render, redirect
from django.urls import reverse

from .models import FileForm


def read(request):
    data = FileForm.objects.all()
    return render(request, 'formwithfile/index.html', {'data': data})


def create(request):
    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        file = request.FILES.get('file')

        obj = FileForm(
            username=username,
            email=email,
            password=password,
            file=file,
        )

        obj.save()

        # return redirect(revserse('read'))
        return redirect('/')

    return render(request, 'formwithfile/form.html')


def update(request, id):
    try:
        data = FileForm.objects.get(id=id)
    except:
        return render(request, 'formwithfile/index.html')

    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            file = request.FILES.get('file', "")
        except:
            file = ""

        data.username = username
        data.email = email
        data.passsword = password

        if file != "":
            data.file = file

        data.save()

        # return redirect(reverse('read'))
        return redirect('/')

    return render(request, 'formwithfile/update.html', {"data": data})


def delete(request, id):
    if request.method == "POST":
        try:
            obj = FileForm.objects.get(id=id)
            obj.delete()
        except:
            return render(request, 'formwithfile/index.html')

    return render(request, 'formwithfile/index.html')
