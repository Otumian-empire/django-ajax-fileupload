from django.shortcuts import render, redirect


def read(request):
    return render(request, 'formwithfile/index.html')

def create(request):
    # return redirect('read', 'formwithfile/form.html')
    return render(request, 'formwithfile/form.html')

def update(request):
    return redirect('read')

def delete(request):
    return redirect('read')



