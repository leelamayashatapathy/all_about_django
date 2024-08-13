# middleware.py

import threading

# Thread-local variable to store the request
_thread_locals = threading.local()

def get_current_request():
    """Returns the current request stored in thread-local storage."""
    return getattr(_thread_locals, 'request', None)

class ThreadLocalMiddleware:
    """Middleware that saves the request in thread-local storage."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.request = request
        response = self.get_response(request)
        return response
