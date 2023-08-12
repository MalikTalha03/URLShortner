from django.shortcuts import render,redirect
import pyshorteners
# Create your views here.
def home(request):
    short_url = None  # Initialize short_url to None
    
    if request.method == 'POST':
        url = request.POST['url']
        short = pyshorteners.Shortener()
        short_url = short.tinyurl.short(url)  # Assign the shortened URL
        context = {'short_url': short_url}  # Pass the short_url to the template context
        return render(request, 'shorturl.html', context)
    return render(request, 'home.html')