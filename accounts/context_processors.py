from .models import SystemSettings

def system_settings(request):
    """
    Globally inject SystemSettings into all Django templates
    so that variables like theme_color are always accessible as `sys_settings`.
    """
    settings = SystemSettings.get_settings()
    return {'sys_settings': settings}
