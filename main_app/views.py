from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
#...
from django.views.generic.base import TemplateView
from .models import Artist
# For create route; Import to extend from class::
from django.views.generic.edit import CreateView
# For showing details:
from django.views.generic import DetailView

# Create your views here.

# Here we will be creating a class called Home and extending it from the View class
class Home(TemplateView):
    template_name = 'home.html'
    # Here we are adding a method that will be ran when we are dealing with a GET request
    #def get(self, request):
        # Here we are returning a generic response
        # This is similar to response.send() in express
        #return HttpResponse("Spotify Home")
    
class About(TemplateView):
    template_name = 'about.html'
    #def get(self, request):
        #return HttpResponse('Spotify About')

class ArtistList(TemplateView):
    template_name = 'artist_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Access query param for search
        name = self.request.GET.get("name")
        # Filter by name if query exists
        if name != None:
            #.filter is the sql WHERE statement and name__icontains is doing a search for any name with the query param
            context['artists'] = Artist.objects.filter(name__icontains=name)
            # Dynamic header
            context['header'] = f"Searching for {name}" 
        else:
            context['artists'] = Artist.objects.all() # Use the model to query the database
            context['header'] = "Trending Artists"
        return context

class ArtistCreate(CreateView):
    model = Artist
    fields = ['name', 'img', 'bio', 'verified_artist']
    template_name = 'artist_create.html/'
    success_url = '/artists/'
    
class ArtistDetail(DetailView):
    model = Artist
    template_name = 'artist_detail.html'