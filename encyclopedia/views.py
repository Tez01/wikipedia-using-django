from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render
import datetime
import markdown
from django.http import HttpResponse
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import util

def index(request):
    # Check if method is post
    if request.method == "POST":
        if 'q' in request.POST:
            title = request.POST.get("q")
        elif 'submit_param' in request.POST:
            title = request.POST.get("submit_param")
            #Fetch the entry
            entry = util.get_entry(title)

        #redirect to the required page
        return HttpResponseRedirect(reverse("encyclopedia:openTitle", args=(title,)))
        
        
            

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def openTitle(request, title):
    #Fetch the entry
    entry = util.get_entry(title)

    #Check if entry is valid
    if util.get_entry(title) != None:

        #Create html from markdown
        html = markdown.markdown(entry)
        return HttpResponse(f"{html}")
    else:

        #Print error
        return HttpResponse("<h1>The page does not exist</h1>")