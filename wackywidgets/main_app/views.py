from tkinter import W
from django.shortcuts import render
from django.http import HttpResponse
from .models import Widget
from .forms import WidgetForm
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.

class WidgetDelete(DeleteView):
    model = Widget
    success_url = "/"
    template_name = "delete.html"

def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request, 'home.html', {'widgets': widgets, 'widget_form': widget_form} )

def add_widget(request):
    form = WidgetForm(request.POST)
    if form.is_valid():
        new_widget = form.save(commit=False)
        new_widget.save()
    # LOADS HOME PAGE AGAIN
    return redirect('/')



