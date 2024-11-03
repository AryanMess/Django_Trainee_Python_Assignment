import logging
import time
from django.dispatch import Signal, receiver
wfrom django.conf import settings

# Configure Django settings manually
settings.configure(
    DEBUG=True,
    LOGGING={
        'version': 1,
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
            },
        },
        'root': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
)