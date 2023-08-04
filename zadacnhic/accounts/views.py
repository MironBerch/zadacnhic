from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetCompleteView,
    PasswordResetConfirmView,
    PasswordResetDoneView,
    PasswordResetView,
)
from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import View
from django.views.generic.base import TemplateResponseMixin

from accounts.forms import SignUpForm
from accounts.mixins import AnonymousUserRequiredMixin


class SignUpView(
    AnonymousUserRequiredMixin,
    TemplateResponseMixin,
    View,
):
    """View for creating a new account."""

    form_class = SignUpForm
    template_name = 'registration/signup.html'

    def get(self, request: HttpRequest, *args, **kwargs):
        return self.render_to_response(
            context={
                'form': self.form_class(),
            },
        )

    def post(self, request: HttpRequest, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()
            return redirect('signin')

        return self.render_to_response(
            context={
                'form': form,
            },
        )


class SignInView(
    AnonymousUserRequiredMixin,
    LoginView,
):
    """View for signing in."""

    template_name = 'registration/signin.html'


class SignOutView(LogoutView):
    """View for signing out."""

    template_name = 'registration/signout.html'
    next_page = None


class PasswordResetView(PasswordResetView):
    """View for resetting a password."""

    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('password_reset_done')
    html_email_template_name = 'registration/password_reset_email.html'
    email_template_name = 'registration/password_reset_email.html'


class PasswordResetDoneView(PasswordResetDoneView):
    """View for show that resetting a password is done."""

    template_name = 'registration/password_reset_done.html'


class PasswordResetConfirmView(PasswordResetConfirmView):
    """View for confirm resetting a password."""

    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


class PasswordResetCompleteView(PasswordResetCompleteView):
    """View for show that resetting a password is complete."""

    template_name = 'registration/password_reset_complete.html'
