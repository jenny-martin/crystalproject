from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Crystal, Lore
from .forms import ChargingForm

class CrystalCreate(LoginRequiredMixin, CreateView):
  model = Crystal
  fields = ['name', 'color', 'mining', 'uses']
  success_url='/crystals/'   

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class CrystalUpdate(LoginRequiredMixin, UpdateView):
  model=Crystal
  fields=['color', 'mining', 'uses']

class CrystalDelete(LoginRequiredMixin, DeleteView):
  model=Crystal
  success_url='/crystals/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def crystals_index(request):
    crystals = Crystal.objects.filter(user=request.user)
    return render(request, 'crystals/index.html', {'crystals': crystals })

@login_required
def crystals_detail(request, crystal_id):
  crystal = Crystal.objects.get(id=crystal_id)
  lores_crystal_doesnt_have = Lore.objects.exclude(id__in=crystal.lores.all().values_list('id'))
  charging_form = ChargingForm()
  return render(request, 'crystals/detail.html', { 'crystal': crystal, 'charging_form': charging_form, 'lores': lores_crystal_doesnt_have })

@login_required
def add_charging(request, crystal_id):
  form = ChargingForm(request.POST)
  if form.is_valid():
    new_charging = form.save(commit=False)
    new_charging.crystal_id = crystal_id
    new_charging.save()
  return redirect('detail', crystal_id=crystal_id)


class LoreList(LoginRequiredMixin, ListView):
  model = Lore

class LoreDetail(LoginRequiredMixin, DetailView):
  model = Lore

class LoreCreate(LoginRequiredMixin, CreateView):
  model = Lore
  fields = '__all__'

class LoreUpdate(LoginRequiredMixin, UpdateView):
  model = Lore
  fields = '__all__'

class LoreDelete(LoginRequiredMixin, DeleteView):
  model = Lore
  success_url = '/uses/'

@login_required
def assoc_lore(request, crystal_id, lore_id):
  Crystal.objects.get(id=crystal_id).lores.add(lore_id)
  return redirect('detail', crystal_id=crystal_id)

@login_required
def unassoc_lore(request, crystal_id, lore_id):
  Crystal.objects.get(id=crystal_id).lores.remove(lore_id)
  return redirect('detail', crystal_id=crystal_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)