from django.utils.deprecation import MiddlewareMixin
from django.urls import resolve

class DisableCSRFOnToken(MiddlewareMixin):
    def process_request(self, request):
        # Obtiene el nombre de la vista que corresponde a la URL actual
        resolver_match = resolve(request.path)
        
        # Si la vista es para obtener o refrescar token, desactiva CSRF
        if resolver_match.url_name in ['token_obtain_pair', 'token_refresh']:
            setattr(request, '_dont_enforce_csrf_checks', True)
