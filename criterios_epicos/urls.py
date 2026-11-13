from django.urls import path
from .views import (EpicoListView, EpicoCreateView, EpicoUpdateView, EpicoDetailView, EpicoDeleteView, HistoriaUsuarioCreateView, HistoriaUsuarioDeleteView, HistoriaUsuarioDetailView, HistoriaUsuarioListView, HistoriaUsuarioUpdateView, CriterioCreateView, CriterioListView, CriterioDeleteView, CriterioDetailView, CriterioUpdateView)

app_name = 'criterios_epicos'

urlpatterns =[
    path('epico/', EpicoListView.as_view(), name= 'epico_list'),
    path('epico/novo/', EpicoCreateView.as_view(), name= 'epico_create'),
    path('epico/<int:pk>/editar/', EpicoUpdateView.as_view(), name= 'epico_update'),
    path('epico/<int:pk>/', EpicoDetailView.as_view(), name= 'epico_detail' ),
    path('epico/<int:pk>/excluir/', EpicoDeleteView.as_view(), name= 'epico_delete'),
    #rotas historia de usuario
    path('historia/', HistoriaUsuarioListView.as_view(), name='historia_list'),
    path('historia/novo/', HistoriaUsuarioCreateView.as_view(), name='historia_create'),
    path('historia/<int:pk>/editar/', HistoriaUsuarioUpdateView.as_view(), name='historia_update'),
    path('historia/<int:pk>/', HistoriaUsuarioDetailView.as_view(), name='historia_detail'),
    path('historia/<int:pk>/excluir', HistoriaUsuarioDeleteView.as_view(), name='historai_excluir'),
    #rotas historia 
    path('criterio/', CriterioListView.as_view(), name='criterio_list'),
    path('criterio/novo/', CriterioCreateView.as_view(), name='criterio_create'),
    path('criterio/<int:pk>/editar', CriterioUpdateView.as_view(), name='criterio_update'),
    path('criterio/<int:pk>/', CriterioDetailView.as_view(), name='criterio_detail'),
    path('criterio/<int:pk>/delete/', CriterioDeleteView.as_view(), name='criterio_detail'),
]