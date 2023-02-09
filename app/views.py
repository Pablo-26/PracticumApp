#Conector de python con mysql
import mysql.connector as mysql
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render,redirect
import requests
import json

def home(request):
    return render(request, 'home.html')

def search(word):

    db = mysql.connect(
        host="localhost",
        user="root",
        password="Pablo260104.",
        database="db"
    )
    cursor = db.cursor()

    cursor = db.cursor(dictionary=True)
    query = "SELECT * FROM movies"
    execute = cursor.execute(query)
    data = cursor.fetchall()

    resultado = list(filter(lambda x: word in x['title'], data))
    return resultado


def procesar(request):
    word = request.GET.get('word', '')
    temple = open("C:/Users/Personal/PycharmProjects/Practicum/templates/results.html")
    template = Template(temple.read())
    temple.close()
    ctx = Context({'result': search(word)})
    doc = template.render(ctx)
    return HttpResponse(doc)
