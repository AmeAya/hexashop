from django.shortcuts import render


def homeView(request):
    return render(request, template_name='index.html', context={})
