# Django5 README

## Auth 

##### ***"  -  " means DELETED LINES***
##### ***"  +  " means ADDED LINES***

### To use TokenAuthentication instead of BasicAuthenticaton:
1. Add a new app to the project/settings.py:
    ```bash
    # marryme/settings.py

    # ...

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'budget',
        'rest_framework',
    +   'rest_framework.authtoken',
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
    -       'rest_framework.authentication.BasicAuthentication',
    +       'rest_framework.authentication.TokenAuthentication',
        ],
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAuthenticated',
        ],
    }
    # ...
    ```

2. Create a route to send user credentials to receive a token:
    ```bash
    # marryme/urls.py


    from django.contrib import admin
    from django.urls import path, include
    + from rest_framework.authtoken.views import obtain_auth_token

    urlpatterns = [
        path('admin/', admin.site.urls),
    +    path('login/', obtain_auth_token, name='login'),
        path('', include('budget.urls')),
    ]

    ```

3. Update app/views.py to auth with Tokens:
    ```bash
    # budget/views.py


    from rest_framework import viewsets
    from .models import Vendor, Marriage, Budget
    - from rest_framework.authentication import BasicAuthentication
    + from rest_framework.authentication import TokenAuthentication
    from .serializers import (AdminVendorSerializer,
                            VendorSerializer,
                            MarriageSerializer,
                            BudgetSerializer)
    from .permissions import IsOwnerOrAdmin


    class VendorViewSet(viewsets.ModelViewSet):
        queryset = Vendor.objects.all()
        serializer_class = AdminVendorSerializer
    -   authentication_classes = [BasicAuthentication]
    +   authentication_classes = [TokenAuthentication]

        def get_serializer_class(self):
            if self.action in ("create", "destroy", "update"):
                return AdminVendorSerializer
            return VendorSerializer


    class MarriageViewSet(viewsets.ModelViewSet):
        queryset = Marriage.objects.all()
        serializer_class = MarriageSerializer
    -   authentication_classes = [BasicAuthentication]
    +   authentication_classes = [TokenAuthentication]
        permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Marriage.objects.all()
        else:
            return Marriage.objects.filter(user=self.request.user)


    class BudgetViewSet(viewsets.ModelViewSet):
        queryset = Budget.objects.all()
        serializer_class = BudgetSerializer
    -   authentication_classes = [BasicAuthentication]
    +   authentication_classes = [TokenAuthentication]
        permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Budget.objects.all()
        else:
            return Budget.objects.filter(user=self.request.user)
    ```


### To use SimpleJWT:
1. Install the following module:
    ```bash
    pip install djangorestframework-simplejwt
    ```

2. Add a new app to the project/settings.py:
    ```bash
    # marryme/settings.py

    INSTALLED_APPS = [
        # ...
        'rest_framework',
    -   'rest_framework.authtoken',
    +   'rest_framework_simplejwt',
        # ...
    ]

    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': [
    -       'rest_framework.authentication.TokenAuthentication',
    +       'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
        # Outras configurações do DRF ...
    }
    ```

3. Update routes:
    ```bash
    # marryme/urls.py


    from django.urls import path, include
    - from rest_framework.authtoken.views import obtain_auth_token
    + from rest_framework_simplejwt.views import (TokenObtainPairView,
    +                                             TokenRefreshView,
    +                                             TokenVerifyView)

    urlpatterns = [
        path('admin/', admin.site.urls),
    -   path('login/', obtain_auth_token, name='login'),
    +   path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    +   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    +   path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('', include('budget.urls')),
    ]
    ```

4. Update app/views.py to auth with SimpleJWT:
    ```bash
    from rest_framework import viewsets
    from .models import Vendor, Marriage, Budget
    - from rest_framework.authentication import TokenAuthentication
    from .serializers import (AdminVendorSerializer,
                            VendorSerializer,
                            MarriageSerializer,
                            BudgetSerializer)
    from .permissions import IsOwnerOrAdmin


    class VendorViewSet(viewsets.ModelViewSet):
        queryset = Vendor.objects.all()
        serializer_class = AdminVendorSerializer
    -   authentication_classes = [TokenAuthentication]

        def get_serializer_class(self):
            if self.action in ("create", "destroy", "update"):
                return AdminVendorSerializer
            return VendorSerializer




    class MarriageViewSet(viewsets.ModelViewSet):
        queryset = Marriage.objects.all()
        serializer_class = MarriageSerializer
    -   authentication_classes = [TokenAuthentication]
        permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Marriage.objects.all()
        else:
            return Marriage.objects.filter(user=self.request.user)


    class BudgetViewSet(viewsets.ModelViewSet):
        queryset = Budget.objects.all()
        serializer_class = BudgetSerializer
    -   authentication_classes = [TokenAuthentication]
        permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Budget.objects.all()
        else:
            return Budget.objects.filter(user=self.request.user)
    ```
