# This is session_manager section

import time

import uuid  # To generate unique session IDs

class SessionManager:
    def __init__(self, session_lifetime=60):
       
        self.session_lifetime = session_lifetime
        self.sessions = {}  # {session_id: expiry_timestamp}
    
    def create_session(self, user_id):
        
        session_id = str(uuid.uuid4())  # Unique session ID
        expiry_time = time.time() + self.session_lifetime
        self.sessions[session_id] = {"user_id": user_id, "expiry": expiry_time}
        return session_id
    
    def is_session_valid(self, session_id):
        
        current_time = time.time()
        session = self.sessions.get(session_id)
        
        if not session:
            return False
        
        if current_time > session["expiry"]:
            # Session expired → remove it
            del self.sessions[session_id]
            return False
        
        return True
    
    def cleanup_expired_sessions(self):
       
        current_time = time.time()
        expired = [sid for sid, data in self.sessions.items() if data["expiry"] < current_time]
        for sid in expired:
            del self.sessions[sid]


if __name__ == "__main__":
    sm = SessionManager(session_lifetime=5)  # Sessions expire in 5 seconds
    
    user = "user_123"
    session_id = sm.create_session(user)
    print(f"New session created: {session_id}")
    
    for i in range(7):
        is_valid = sm.is_session_valid(session_id)
        print(f"Check {i+1}: Session {'valid' if is_valid else 'expired'}")
        time.sleep(1.5)
