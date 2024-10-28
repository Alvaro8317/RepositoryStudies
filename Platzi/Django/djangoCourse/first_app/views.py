from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

from .models import Car


class CarListView(TemplateView):
    template_name = 'car_list.html'

    def get_context_data(self):
        return {
            "car_list": Car.objects.all(),
        }


def my_view(request):
    cars = Car.objects.all()
    context = {
        "car_list": cars,
    }
    return render(request, 'car_list.html', context)


def list_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    if kwargs.get("identifier"):
        return HttpResponse(f"Hola, enviaste {kwargs["identifier"]} como identificador")
    if kwargs.get("brand"):
        return HttpResponse(f"Hola, enviaste {kwargs['brand']} como marca")
    return HttpResponse("Hola tú, estás en la vista de listar")
