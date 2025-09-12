import time


class RateLimiter:
    def __init__(self, max_requests, window_seconds):
       
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.user_requests = {}  # {user_id: [timestamps]}
    
    def is_allowed(self, user_id):
       
        current_time = time.time()
        
        if user_id not in self.user_requests:
            self.user_requests[user_id] = []
        
        # Filter out timestamps older than the time window
        self.user_requests[user_id] = [
            t for t in self.user_requests[user_id] 
            if t > current_time - self.window_seconds
        ]
        
        if len(self.user_requests[user_id]) < self.max_requests:
            # Allow the request
            self.user_requests[user_id].append(current_time)
            return True
        else:
            # Block the request
            return False



if __name__ == "__main__":
    # Allow 3 requests per user in a 10-second window
    limiter = RateLimiter(max_requests=3, window_seconds=10)

    user = "user_1"

    for i in range(5):
        if limiter.is_allowed(user):
            print(f"Request {i+1} ✅ allowed")
        else:
            print(f"Request {i+1} ❌ blocked")
        time.sleep(2)
