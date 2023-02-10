from django.shortcuts import render
from django.views.generic import TemplateView
from .models import MedicalCondition
import requests


def HomePageView(request):
    url = "http://hapi.fhir.org/baseR4/Condition?_pretty=true"
    response = requests.get(url)
    data = response.json()
    data_list = []
    data_id_list = []
    data_last_updated_list = []
    data_display_list = []
    for item in data["entry"]:
        data_list.append(item)
    for item in data_list:
        data_id_list.append(item["resource"]["id"])
        data_last_updated_list.append(item["resource"]["meta"]["lastUpdated"])
        data_display_list.append(item["resource"]["code"]["coding"][0]["display"])

    result_data_list = list(
        zip(data_id_list, data_last_updated_list, data_display_list)
    )

    return render(
        request,
        "home.html",
        {'db' : result_data_list},
    )


def CreatePageView(request):
    return render(request, "create_data.html")


def EditPageView(request , id):
    record = MedicalCondition.objects.get(record_id = id)
    return render(request, "edit_data.html")


def DeletePageView(request):
    return render(request, "delete_data.html")
