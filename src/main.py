from fastapi import FastAPI, Request, UploadFile, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
import aiofiles
import os
from fastapi.templating import Jinja2Templates
from web import uploads, search
from pathlib import Path


app = FastAPI()
app.include_router(uploads.router)
app.include_router(search.router)

if __name__ == "__main__":

    import uvicorn
    uvicorn.run("main:app", reload=True)