from django.urls import path
from .views import EpicoListView, EpicoCreateView, EpicoUpdateView, EpicoDetailView, EpicoDeleteView

urlpatterns =[
    path('criterios_epicos/epico/', EpicoListView.as_view(), name= 'epico_list'),
    path('criterios_epicos/epico/novo/', EpicoCreateView.as_view(), name= 'epico_create'),
    path('criterios_epicos/epico/<int:pk>/editar/', EpicoUpdateView.as_view(), name= 'epico_update'),
    path('criterios_epicos/epico/<int:pk>/', EpicoDetailView.as_view(), name= 'epico_detail' ),
    path('criterios_epicos/epico/<int:pk>/excluir/', EpicoDeleteView.as_view(), name= 'epico_excluir')
]