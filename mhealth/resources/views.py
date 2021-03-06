from django.views import generic
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
import json
from .serializers import *
from django.db import connection


def dictfetchall(cursor):
    "Return all rows from a cursor as a dict"
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def resource_list_by_location(request, category_id, lat, lon):
    #resources = Resources.objects.filter(category_id = category_id)
    cursor = connection.cursor()
    cursor.execute("select * from (SELECT  *,( 3959 * acos( cos( radians("+lat+") ) * cos( radians( latitude ) ) * cos( radians( longitude ) - radians("+lon+") ) + sin( radians("+lat+") ) * sin( radians( latitude ) ) ) ) AS distance FROM resources_resources) al where distance < 50000000 and category_id = "+category_id+" ORDER BY distance limit 5");
    listTemp = dictfetchall(cursor)
    cursor.close()
    return render(request, 'resources/index.html',
                 {'resources': listTemp, "resources2": json.dumps(listTemp), "latitude" : lat, "longitude" : lon})

def home(request):
    return render(request, 'resources/home.html')

def category_list(request):
    category = Category.objects.all
    return render(request, 'resources/category_list.html',
                 {'categories': category})

def resource_list(request,pk):
    resource = Resources.objects.filter(category_id=pk)
    return render(request, 'resources/resource_list.html',
                 {'resources': resource, 'category_id': pk})

def feedback(request):
    return render(request, 'resources/feedback.html')

def about_us(request):
    return render(request, 'resources/about_us.html',
                 {})