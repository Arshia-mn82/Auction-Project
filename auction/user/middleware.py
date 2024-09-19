import logging
from datetime import datetime


logger = logging.getLogger(__name__)
logging.basicConfig(
    filename="request_logs.log", level=logging.INFO, format="%(message)s"
)


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user = request.user if request.user.is_authenticated else "Anonymous"
        endpoint = request.path
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ip = request.META.get("REMOTE_ADDR", "Unknown IP")

        logger.info(f"User: {user}, Endpoint: {endpoint}, Time: {time}, IP: {ip}")

        response = self.get_response(request)
        return response
