
from django.urls import path
from .views import CreateAccountView, AccountView

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
    name='createAccount'),
    path('<int:pk>', AccountView.as_view(), name='profile'),
]
# -----------------------
    # FUNCTION:
    # <INSERT>

    # ASSIGNMENT:
    # <INSERT>

    # REFERENCES:
    # ID PK to identify individual users

    # ALTERNATIVE SOLUTIONS:
    # {% comment %}

        # ALTERNATIVE 1:
            # from django.urls import path
            # from .views import CreateAccountView, AccountView
            # app_name = 'users'
            # urlpatterns = [
            #     path('create-account/', CreateAccountView.as_view(),
            #     name='createAccount'),
            #     path('view-account/', AccountView.as_view(), 
            #     name='account')
            #     path('<int:pk>', AccountView.as_view(), name='profile')

    # {% endcomment %}