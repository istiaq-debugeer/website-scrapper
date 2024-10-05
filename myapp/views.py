from django.shortcuts import render
import requests

from .models import model
from bs4 import BeautifulSoup
from django.http import HttpResponseRedirect
def scrape(request):
    if request.method == "POST":
        site=request.POST.get('site')
        if site:
            model.objects.all().delete()
            page=requests.get(site)
            soup=BeautifulSoup(page.text,'html.parser')

        
            
            for link in soup.find_all('a'):
                link_address=link.get('href')
                link_text=link.string
                if link_address and link_text:  # Ensure both address and text are valid
                    model.objects.create(address=link_address, name=link_text)
                
        
        return HttpResponseRedirect('/')
    else:
        data=model.objects.all()  
    return render(request,'result.html',{'data':data})           
        
     

def delete_link(request):
    
    return render(request,'')
