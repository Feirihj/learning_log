from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class BootstrapMixin:
    """Добавляет Bootstrap-класс всем полям формы."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"


class LoginForm(BootstrapMixin, AuthenticationForm):
    pass


class RegisterForm(BootstrapMixin, UserCreationForm):
    pass
