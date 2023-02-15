from django.shortcuts import render 
import json
from django.views.generic import TemplateView
from .models import MedicalCondition
import requests


def HomePageView(request):
    url = "http://hapi.fhir.org/baseR4/Condition"
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
    url = "http://hapi.fhir.org/baseR4/Condition"  
    if request.method == 'POST':
        display = request.POST.get('display')
        payload =  {"display": display}
        condition_json = json.dumps(payload)
        headers = {"Content-Type": "application/fhir+json"}
        response = requests.post(url, headers=headers, data=condition_json)
        temp_data = response.json()
        print(temp_data)
        if response.status_code == 201:
            print("Condition resource created successfully")
        else:
            print("Error creating  resource: ", response.text)
    return render(request, 'create_data.html')


def EditPageView(request):
    url = "http://hapi.fhir.org/baseR4/Condition"  
    if request.method == 'POST':
        id = request.POST.get('id')
        updated_data = {'display': request.POST.get('display'), 'id':id}
        headers = {"Content-Type": "application/fhir+json"}
        print(updated_data)
        condition_json = json.dumps(updated_data)
        response = requests.put(url + "/" + str(id), headers=headers, data=condition_json)
        temp_data = response.json()
        print(temp_data)
        if response.status_code == 200:
            print("condition resource created successfully")
        else:
            print("Error creating  resource: ")
    return render(request, "edit_data.html")


def DeletePageView(request):
    url = "http://hapi.fhir.org/baseR4/Condition"  
    if request.method == 'POST':
        id = request.POST.get('id')
        response =requests.delete(url + "/" + str(id))
        temp_data = response.json()
        print(temp_data)  
        if response.status_code == 204:
            print('Resource deleted successfully.')
        else:
            print('Error deleting resource: ', response.status_code, response.reason)      
    return render(request, "delete_data.html")
