# Configure logging
from . import Settings
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define a custom signal
my_signal = Signal()

# Define a receiver that simulates a long-running task
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    logger.info("Receiver started")
    time.sleep(5)  # Simulate a delay
    logger.info("Receiver finished")

# Define a function that mimics the view
def my_view():
    start_time = time.time()
    logger.info("View started")

    # Trigger the signal
    my_signal.send(sender=None)

    logger.info("View finished")
    end_time = time.time()

    return f"Total time taken: {end_time - start_time} seconds"

# Execute the "view"
output = my_view()
print(output)