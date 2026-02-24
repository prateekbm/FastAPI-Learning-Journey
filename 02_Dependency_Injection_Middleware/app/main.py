from fastapi import FastAPI
from .middleware import LoggingMiddleware
from .exceptions import CustomException, custom_exception_handler
from .routes import router

app = FastAPI(title="Dependency Injection & Middleware API")

# Add middleware
app.add_middleware(LoggingMiddleware)

# Add custom exception handler
app.add_exception_handler(CustomException, custom_exception_handler)

# Include routes
app.include_router(router)