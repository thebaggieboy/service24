from django.urls import include, path


from . import views

app_name = 'core'



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', views.RentalView.as_view(), name='rentals'),
    path('apartment/<int:pk>', views.ApartmentDetailView.as_view(), name='detail'),
    path('get_started/', views.GetStartedView.as_view(), name='get_started'),
    path('become_a_host/', views.BecomeAHostView.as_view(), name='host'),
    path('register', views.RegisterView.as_view(), name='register'),
   

   
  
]