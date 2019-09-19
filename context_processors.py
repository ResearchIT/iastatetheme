from django.apps import apps

def theme_config(request):
    return {'iastatetheme_config': apps.get_app_config('iastatetheme')}