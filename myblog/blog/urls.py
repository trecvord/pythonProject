# --------------------------------------------------
#
# Program by R. Kholmurotov.
#
#
#  Version        Date           Info
#  1.0            2023      Autumn Version
#
# -----------------PRACTICE-------------------------

from django.urls import path
from . import views

urlpatterns = [path('', views.PostView.as_view())]