import logging
import time
from fastapi import FastAPI, HTTPException, Depends, Request
from app.schemas import LinkCreate, Link
from app.services.link_service.link_service import LinkService
from fastapi.middleware.cors import CORSMiddleware

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Example CORS settings (if needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Custom logging middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    
    # Log request details
    logger.info(f"Incoming request: {request.method} {request.url}")
    
    # Process request
    response = await call_next(request)

    # Measure execution time
    process_time = time.time() - start_time

    # Log response details
    logger.info(
        f"Completed {request.method} {request.url} "
        f"with status {response.status_code} in {process_time:.2f} sec"
    )

    return response

# Dependency injection of LinkService
@app.post("/shorten", response_model=Link, status_code=201)
def shorten_url(link: LinkCreate, service: LinkService = Depends()):
    res = service.shorten(link)
    return res

@app.get("/{short_code}", response_model=Link)
def get_link(short_code: str, service: LinkService = Depends()):
    link = service.get_by_code(short_code)
    if not link:
        raise HTTPException(status_code=404, detail="Link not found")
    return link

