from django.urls import path
from .router import router

from .views import      UsuariosListView    \
                    ,   UsuariosDetailView  \
                    ,   UsuariosCreateView  \
                    ,   UsuariosUpdateView  \
                    ,   UsuariosDeleteView

app_name = "hidro"

urlpatterns = [
    path("", UsuariosListView.as_view(), name="all"),
    path("create/", UsuariosCreateView.as_view(), name="create"),
    path("<int:pk>/detail/", UsuariosDetailView.as_view(), name="detail"),
    path("<int:pk>/update/", UsuariosUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", UsuariosDeleteView.as_view(), name="delete"),
]

urlpatterns += router.urls