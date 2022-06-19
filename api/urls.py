from django.urls import include, path
from .routes import router




# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
   
   path('', include(router.urls))
]