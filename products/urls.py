from django.urls import path
from . import views

urlpatterns = [
    path("",views.home),
    path("about/",views.about,name="aboutpage"),
    path("menu/",views.products,name="menu"),
    path("search/",views.search),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    path("logout/",views.logout,name="logout"),
    path("add_to_cart/",views.addtocart,name="add-to-cart"),
    path("cart/",views.cart,name="cart"),
    path("cart/quantitymore/<int:id>",views.quantitymore),
    path("cart/quantityless/<int:id>",views.quantityless),
    path("profile/",views.profile,name="profile"),
]