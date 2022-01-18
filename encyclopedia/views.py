from datetime import datetime
from http.client import HTTPResponse
from django.shortcuts import render
import datetime
import markdown
from django.http import HttpResponse

from . import util
from django.core.files.storage import default_storage

def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None
def index(request):
    # Check if method is post
    if request.method == "POST":
        title = request.POST.get("q")

        #Fetch the entry
        entry = get_entry(title)

        #Check if entry is valid
        if get_entry(title) != None:

            #Create html from markdown
            html = markdown.markdown(entry)
            return HttpResponse(f"{html}")
        else:

            #Print error
            return HttpResponse("<h1>The page does not exist</h1>")
            

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

