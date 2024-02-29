from django.forms import ModelForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.models import UserModel


class UserForm(ModelForm):
    class Meta:
        model = UserModel
        fields = "__all__"








