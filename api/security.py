from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Simple bearer token mechanism
security = HTTPBearer()
SECRET_TOKEN = "our-token-3000"  # we can change this or move to env var

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    if credentials.scheme != "Bearer" or credentials.credentials != SECRET_TOKEN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing token.",
        )
