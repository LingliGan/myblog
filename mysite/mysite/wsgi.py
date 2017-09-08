from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise

application = get_wsgi_application() – this line of code is already present
application = DjangoWhiteNoise(application)
