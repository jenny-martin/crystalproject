from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('crystals/', views.crystals_index, name='index'),
    path('crystals/<int:crystal_id>/', views.crystals_detail, name='detail'),
    path('crystals/create/', views.CrystalCreate.as_view(), name='crystals_create'),
    path('crystals/<int:pk>/update/', views.CrystalUpdate.as_view(), name='crystals_update'),
    path('crystals/<int:pk>/delete/', views.CrystalDelete.as_view(), name='crystals_delete'),
    path('crystals/<int:crystal_id>/add_charging/', views.add_charging, name='add_charging'),
    path('lores/', views.LoreList.as_view(), name='lores_index'),
    path('lores/<int:pk>/', views.LoreDetail.as_view(), name='lores_detail'),
    path('lores/create/', views.LoreCreate.as_view(), name='lores_create'),
    path('lores/<int:pk>/update/', views.LoreUpdate.as_view(), name='lores_update'),
    path('lores/<int:pk>/delete/', views.LoreDelete.as_view(), name='lores_delete'),
    path('crystals/<int:crystal_id>/assoc_lore/<int:lore_id>/', views.assoc_lore, name='assoc_lore'),
    path('crytals/<int:crystal_id>/unassoc_lore/<int:lore_id>/', views.unassoc_lore, name='unassoc_lore'),
    path('accounts/signup', views.signup, name='signup'),
]
