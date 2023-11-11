from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse

# shop/views.py
def storePageView(request):
    url = reverse("home_page")
    page = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title<Our Shop </title>
    </head>
    <body>
    <h1>This is the web store</h1>
    <p>This is the items page</p>
    <a href = "{url}">Home Page</a>
    </body>
    </html>
    
    
    """

    return HttpResponse(page)



