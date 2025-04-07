from rest_framework_simplejwt.authentication import JWTAuthentication

class CookieJWTAuthentication(JWTAuthentication):
    """
    Autenticación personalizada que busca el token en el header y, en caso de no encontrarlo,
    lo busca en la cookie 'access_token'.
    """
    def authenticate(self, request):
        header = self.get_header(request)
        
        if header is None:
            # Si no se encuentra en el header, se intenta obtener de la cookie
            raw_token = request.COOKIES.get('access_token')
        else:
            raw_token = self.get_raw_token(header)
            
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        return self.get_user(validated_token), validated_token