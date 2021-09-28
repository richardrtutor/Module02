from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from dataclasses import dataclass
from typing import Dict,List

@dataclass
class Team:
    title: str
    desc: str
    memb: List[str]

# Create your views here.

def team_page(request, team):
    context = {
        "team": team,
        "team_list": {"procurement": Team(
            "Procurement Team", 
            "As members of the procurement team we make sure that Base Camp has everything that it needs, from groceries to making sure that the other teams have what they need to complete their jobs. We fix and set out lunch for the other students as well as being in charge of a weekly budget provided to us by the board members of the school.", 
             ["Richard Tutor", "Dylan Shipton", "Quinton Summerford", "Ethan Ward", "Mariann McCord", "Gary Lane"]
        ),
        "management":Team(
             "Management Team",
            """
                    As members of the Management team we make sure that Base Camp is properly
      managed, from cleaning, setting chores, and setting meetings. We are in
      charge of making sure that everything that needs to get done, does get
      done.
                    """,
            ["Daelan Hollingsworth", "Michelle Rankin", "Rylee Chisholm", "Dylan Goad", "Logan Coley", "Will Collins"]
        ),
        
        "documentation": Team(
            "Documentation Team",
             """
                    As members of the documentation team we make sure that Base Camp's events
      gets filmed, from presentation to karaoke, we make sure to get snippets of
      it! We post on Instagram, Twitter, Facebook, and Linkedin. There you can
      find guest speakers who have visited us and small articles of whats
      happened at Base Camp.""",
           ["Randy Trullet", "Ryan Bennett", "Makayla Person", "Ben Crosby", "Isaac Jones"]
        ),
        
        "community": Team(
            "Community Team",
            """As members of the Community team we make sure that Base Camp has events!
      From birthday parties to small obstacle courses, you wont find a dull
      community day. The Community team operates hand in hand with the
      Procurement team in order to make sure that everything aligns and no one
      misses out on anything.""",
            ["Jacen Barefoot", "RJay Pickering", "Ariyanna Neil", "Logan Wilkins", "Justin Ashmore"]
        )
        }
    }
   
    return render(request, "teamplate.HTML", context)

    

def home_page(request):
    context = {
        "LPTeams": ["procurement", "management", "documentation", "community"]
    }
    return render(request, "home.HTML", context)