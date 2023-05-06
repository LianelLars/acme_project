from django.contrib import admin
from users.forms import CustomUserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from django.urls import include, path, reverse_lazy

# NEW USER REGISTRATION
User = get_user_model()
# FOR CUTOMIZE 404
handler404 = 'core.views.page_not_found'

auth_patterns = [
    path('', include('django.contrib.auth.urls')),
    path(
      'registration/',
      CreateView.as_view(
          template_name='registration/registration_form.html',
          form_class=CustomUserCreationForm,  # UserCreationForm
          success_url=reverse_lazy('pages:homepage'),
      ),
      name='registration',
    )
]

urlpatterns = [
    path('', include('pages.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include((auth_patterns, 'auth'))),  # NEW USER REGISTRATION
    path('birthday/', include('birthday.urls')),
]
