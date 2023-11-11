from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .data import players
# team/views.py
def homePageView(request):
    url = reverse("about_page")
    url2 = reverse("store_page")
    url3 = reverse("players_page")
    page = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title<Our TEAM </title>
    </head>
    <body>
    <h1>This is the homepage of our Team</h1>
    <p>This is the page with info about our team</p>
    <a href = "{url}">About Page</a>
    <a href = "{url2}">Go to our Shop</a>
    <a href = "{url3}">View our players</a>
    </body>
    </html>
    
    
    """

    return HttpResponse(page)

def teamPageView(request):
    url = reverse("home_page")
    #player_url = reverse("player_data", args=[index])
    page_part1 = """
    <!DOCTYPE html>
    <html>
    <head>
    <title<Our TEAM </title>
    </head>
    <body>
    <h1>Players of our Team</h1>
    <p>This is the page with info about our team</p>
    <ol>
    """
    
    index = 0
    for player in players:
        player_url = reverse("player_data", args=[index])
        page_part1 += (f'<li><a href = "{player_url}">' + player["name"] + "</a></li>")
        index += 1
    
    page_part2 = f"""
    </ol>
    <a href = "{url}">Home Page</a>
    </body>
    </html>
    
    
    """
    return HttpResponse(page_part1 + page_part2)

def playerPageView(request, player_id):
    url = reverse("home_page")
    url2 = reverse("players_page")
    page = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title<Our TEAM </title>
    </head>
    <body>
    <h1>About Player {player_id}</h1>
    <p>Player data</p>
    <P>Name:{players[player_id]["name"]}</p>
    <P>Age:{players[player_id]["age"]}</p>
    <P>Position:{players[player_id]["position"]}</p>
    <a href = "{url}">Home Page</a>
    <a href = "{url2}">Team Page</a>
    </body>
    </html>
    
    
    """

    return HttpResponse(page)




def aboutPageView(request):
    url = reverse("home_page")
    page = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <title<Our TEAM </title>
    </head>
    <body>
    <h1>About</h1>
    <p>Contact data</p>
    <a href = "{url}">Home Page</a>
    </body>
    </html>
    
    
    """

    return HttpResponse(page)