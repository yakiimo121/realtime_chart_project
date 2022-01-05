from django.shortcuts import render


def epochjs(request):
    return render(request, 'epochjs.html', {})


def webglplot(request):
    return render(request, 'webglplot.html', {})
