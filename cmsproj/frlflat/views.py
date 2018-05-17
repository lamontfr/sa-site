from django.http import HttpResponseRedirect
from django.utils import translation
from django.views import generic

# Create your views here.
class SetLanguage(generic.View):

    def get(self, request, *args, **kwargs):
        user_language = request.GET.get("lang")
        translation.activate(user_language)
        request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        url = request.GET.get('url', '/')
        # print(' _*** SetLanguage, user_language =', user_language,
        #       'url=', url)
        return HttpResponseRedirect(url)
