# middlewares.py

import time
from django.core.cache import cache
from django.conf import settings
from django.http import JsonResponse

class RateLimiterMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.rate_limit = 60  # Number of requests
        self.interval = 60    # Time window in seconds (e.g., 60 seconds)

    def __call__(self, request):
        user_id = request.user.id if request.user.is_authenticated else request.META.get('REMOTE_ADDR')
        cache_key = f"rl:{user_id}"
        current_time = int(time.time())

        # Get current request count and timestamps
        request_data = cache.get(cache_key, [])
        request_data = [timestamp for timestamp in request_data if timestamp > current_time - self.interval]

        if len(request_data) >= self.rate_limit:
            return JsonResponse({'error': 'Rate limit exceeded. Please try again later.'}, status=429)

        request_data.append(current_time)
        cache.set(cache_key, request_data, timeout=self.interval)

        response = self.get_response(request)
        return response
