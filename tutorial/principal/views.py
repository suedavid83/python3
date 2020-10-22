from django.shortcuts import render, redirect
from django.utils import translation
from django.conf.urls import i18n
from .functions import setSystemIdioma, getIdiomaSystem


def setIdioma(request, idioma):
    if translation.LANGUAGE_SESSION_KEY in request.session:
        del request.session[translation.LANGUAGE_SESSION_KEY]
    translation.activate(idioma)
    request.session['django_language'] = idioma
    request.session[translation.LANGUAGE_SESSION_KEY] = idioma
    return redirect("/" + idioma + "/tutorial/")

def home(request):
    return render(request, "index.html")
