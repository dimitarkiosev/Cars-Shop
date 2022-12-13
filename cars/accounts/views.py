from django.urls import reverse_lazy
from django.views import generic as views
from django.contrib.auth import views as auth_views, get_user_model, login
from cars.accounts.forms import UserCreateForm

UserModel = get_user_model()


class SignUpView(views.CreateView):
    model = UserModel
    form_class = UserCreateForm
    template_name = 'accounts/account-register-view.html'
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if self.object:
            login(request, self.object)
        return response


class SignInView(auth_views.LoginView):
    template_name = 'accounts/account-login-view.html'


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('login user')


class AccountDetailsView(views.DetailView):
    model = UserModel
    template_name = 'accounts/account-details-view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['is_owner'] = self.request.user == self.object
        return context


class AccountEditView(views.UpdateView):
    model = UserModel
    template_name = 'accounts/account-edit-view.html'
    fields = ('first_name', 'last_name', 'email', 'phone', 'photo', )

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class AccountDeleteView(views.DeleteView):
    model = UserModel
    template_name = 'accounts/account-delete-view.html'
    success_url = reverse_lazy('index')
