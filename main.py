from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from services.election_logic import ElectionLogic
import os

app = FastAPI(title="Interactive Election Assistant")

# Set up templates
templates_dir = os.path.join(os.path.dirname(__file__), "templates")
templates = Jinja2Templates(directory=templates_dir)

election_service = ElectionLogic()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serve the basic HTML UI from templates."""
    return templates.TemplateResponse(
    request=request, 
    name="index.html", 
    context={"title": "Interactive Election Assistant"}
)

@app.get("/api/journey")
async def get_journey(lang: str = "en", first_time: bool = True):
    """Get the voter journey mapping. Supported languages: 'en' (English), 'gu' (Gujarati)."""
    return election_service.get_voter_journey(language=lang, first_time=first_time)

@app.get("/api/timeline/{city}")
async def get_timeline(city: str):
    """Get the upcoming dummy election dates for a given city."""
    if not city.strip():
        raise HTTPException(status_code=400, detail="City name cannot be empty")
    return election_service.get_timeline(city=city)
