
from django.urls import path
from .views import CreateAccountView, AccountView, ChangePasswordView,ChangePasswordDoneView
from django.contrib.auth import views as auth_views

app_name = 'users'
urlpatterns = [
    path('create-account/', CreateAccountView.as_view(),
    name='createAccount'),
    path('<int:pk>', AccountView.as_view(), name='profile'),

    path('change-password/', ChangePasswordView, name='changePassword'),
    path('change-password-done/', ChangePasswordDoneView, name='changePassword_done'),
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

            # path('change-password/', auth_views.PasswordChangeView.as_view(success_url='users:profile'), name='changePassword'),

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