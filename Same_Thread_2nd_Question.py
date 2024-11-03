# signals.py
from django.dispatch import Signal, receiver
import logging
import threading

# Define a custom signal
my_signal = Signal()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a receiver that logs the thread ID
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    logger.info(f"Receiver running in thread: {threading.get_ident()}")

# views.py
from django.http import HttpResponse
from django.http import HttpRequest
#from .signals import my_signal
import logging
import threading

logger = logging.getLogger(__name__)

def my_view(request):
    logger.info(f"View running in thread: {threading.get_ident()}")

    # Trigger the signal
    my_signal.send(sender=None)

    return HttpResponse("Signal sent")

mock_request = my_view(HttpRequest)
print(mock_request.content.decode())