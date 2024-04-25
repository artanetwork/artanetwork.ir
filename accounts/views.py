from django.contrib.auth.views import PasswordChangeView

from .forms import CustomPasswordChangeForm

# Create your views here.


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
