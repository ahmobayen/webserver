"""webserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'trader'
urlpatterns = [
    path("", views.index, name="index"),
    path("about", TemplateView.as_view(template_name="trader/about.html"), name="about"),
    path("contact", TemplateView.as_view(template_name="trader/contact.html"), name="contact"),
    path("blogs", views.articles, name="blogs"),
    path("market", views.market, name="market"),
    path("chart", TemplateView.as_view(template_name="trader/widgets/chart.html"), name="chart"),
    path("ta_analysis", TemplateView.as_view(template_name="trader/widgets/ta_analysis.html"), name="ta_analysis"),
    path("watchlist", TemplateView.as_view(template_name="trader/widgets/watchlist.html"), name="watchlist"),
    path("load_prices/<str:ticker>", views.load_prices, name="load_prices"),
]

