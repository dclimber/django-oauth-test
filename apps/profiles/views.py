from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        choice = request.POST.get('choice')
        profile = request.user.profile
        if choice == 'Yes':
            profile.in_newsletter = True
        profile.newsletter_offered = True
        profile.save()
        return self.get(request, *args, **kwargs)
