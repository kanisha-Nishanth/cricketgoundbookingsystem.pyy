from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('contact/',views.contact,name='contact'),
    path('search/',views.search,name='search'),
    path('about/',views.about,name='about'),
    path('ground/',views.ground,name='ground'),
    path('book',views.BookPage.as_view(),name='book'),
    path('charge/',views.charge,name='charge'),
    path('bookingpage/',views.bookingpage,name='bookingpage')
    # path("demo",views.new)
]
