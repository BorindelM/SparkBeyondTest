from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request, UploadFile, HTTPException, status, Form
from fastapi.responses import HTMLResponse, RedirectResponse
import aiofiles
import os
from fastapi.templating import Jinja2Templates
from pathlib import Path
from typing import List
from services import search

router = APIRouter(prefix = "/search")

top = Path(__file__).resolve().parent.parent
template_dir = f"{top}/template"
template_obj = Jinja2Templates(directory=template_dir)


@router.get("/")
def top(request: Request):
    files = search.wordsearch_service().get_documents()
    highest_count_word = None
    return template_obj.TemplateResponse("body.html",
        {   "request": request,
            "files": files,
            "highest_count_word": highest_count_word})

@router.post('/')
async def post_upload(request: Request, file: List[str] = Form()):
    files = search.wordsearch_service().get_documents()
    return template_obj.TemplateResponse("body.html",
    {   "request": request,
        "files": files,
        "highest_count_word": search.wordsearch_service().get_most_used_word(file)})

