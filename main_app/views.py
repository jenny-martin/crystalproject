from django.shortcuts import render

class Crystal:
    def __init__(self, name, color, description):
        self.name = name
        self.color = color
        self.description = description
        

crystals = [
    Crystal('Garnet', 'dark red', 'Montana and Idaho'),
    Crystal('Lapis lazuli', 'rich blue hues', 'Afghanistan'),
    Crystal('Onyx', 'black', 'Mexico')
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def crystals_index(request):
    return render(request, 'crystals/index.html', {'crystals': crystals })