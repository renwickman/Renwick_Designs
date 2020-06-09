from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('users', views.createUser),
    path('login', views.login),
    path('profile', views.profile),
    path('portfolio', views.portfolio),
    path('project', views.project),
    path('selectedProject', views.selectedProject),
    path('context', views.context),
    path('selectedContext', views.selectedContext),
    path('location', views.location),
    path('additionalInput', views.additionalInput),
    path('cart', views.cart),
    path('completeService', views.completeService),
    path('checkout', views.checkout),
    path('scheduledConsult', views.scheduledConsult),
    path('logout', views.logout),
    path('homepage', views.homepage)
]


# urlpatterns = [
#     path('', views.index),
#     path('users', views.createUser),
#     path('login', views.login),
#     path('wall', views.wall),
#     path('post_comment', views.comment),
#     path('post_message', views.message),
#     path('delete_comment/<int:id>', views.deleteCom),
#     path('delete_message/<int:id>', views.deleteMes),
#     path('logout', views.logout)
# ]

