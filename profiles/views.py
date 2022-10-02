from django.shortcuts import render
from .models import Profile
from django.views.generic.list import ListView
from .forms import LoginForm, ProfileEditForm
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView
from django.core.files import File
import os
from django.conf import settings



@login_required
def ProfilePage(request):
    profile_id = request.session['_auth_user_id']
    profile = Profile.objects.filter(id=profile_id).first()
    context = {
        'profile': profile,
    }
    return render(request, 'profile.html', context)


class ProfileListView(ListView):
    queryset = Profile.objects.all()
    template_name = 'profiles-list.html'
    context_object_name = 'profiles'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            check_profile = get_user_model().objects.filter(first_name=cd['first_name']).exists()
            if check_profile:
                user = authenticate(first_name=cd['first_name'], password=cd['password'])
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect(reverse('profile'))
                else:
                    context = {
                        'error': 'Error in password',
                        'first_name': cd['first_name']
                    }
                    return render(request, 'login.html', context)
            else:
                context = {
                    'error': 'No such user in database',
                }
                return render(request, 'login.html', context)
        else:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('profiles-list'))


class UpdateProfile(UpdateView):
    model = Profile
    form_class = ProfileEditForm
    template_name = 'profile-edit.html'

    def get_object(self):
        profile_id = self.request.session['_auth_user_id']
        profile = Profile.objects.filter(id=profile_id).first()
        return profile

    def get_success_url(self):
        x_forwarded_for = self.request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = self.request.META.get('REMOTE_ADDR')
        profile_id = self.request.session['_auth_user_id']
        profile = Profile.objects.filter(id=profile_id).first()
        file_path = os.path.join(settings.BASE_DIR, 'user_ip.log')
        f = open(file_path, 'a')
        ip_file = File(f)
        ip_file.write("User ip: " + ip + ' --- Changed profile(id/name): ' + str(profile.id) + '/' + profile.first_name + '\n')
        ip_file.close
        f.close
        return reverse("profiles-list")


