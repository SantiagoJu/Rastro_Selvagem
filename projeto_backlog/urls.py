from django.urls import path
from .views import (ProjetoListView, ProjetoCreateView, ProjetoUpdateView, ProjetoDeleteView, ProjetoDatailView)
from .views import (BacklogListView, BacklogCreateView, BacklogUpdateView, BacklogDeleteView)

urlpatterns = [
    # Projetos
    path('projetos/',ProjetoListView.as_view(), name = 'projeto_list'),
    path('projetos/novo/',ProjetoCreateView.as_view(), name = 'projeto_create'),
    path('projetos/<int:pk>/editar/',ProjetoUpdateView.as_view(), name = 'projeto_update'),
    path('projetos/<int:pk>/excluir/',ProjetoDeleteView.as_view(), name = 'projeto_delete'),
    path('projeto/<int:pk>/',ProjetoDatailView.as_view(), name = 'projeto_datail'),

    # BackLog
    path('backlog/',BacklogListView.as_view(), name = 'backlog_list'),
    path('backlog/novo',BacklogCreateView.as_view(), name = 'backlog_create'),
    path('backlog/<int:pk>/editar/',BacklogUpdateView.as_view(), name = 'backlog_update'),
    path('backlog/<int:pk>/excluir/',BacklogDeleteView.as_view(), name = 'backlog_delete'), 

]