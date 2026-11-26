from django.contrib.auth import login
from django.shortcuts import redirect, render

from .forms import RegisterForm


def register(request):
    """Регистрация нового пользователя."""
    if request.method != "POST":
        form = RegisterForm()
    else:
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Сразу входим под новым пользователем.
            login(request, new_user)
            return redirect("learning_logs:index")
    return render(request, "accounts/register.html", {"form": form})
