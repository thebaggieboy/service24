from django.urls import include, path
from . import views

app_name = 'hosts'



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    #path('', views.HostView.as_view(), name='host'),
    path('', views.host_view, name='get_started'),
   
]