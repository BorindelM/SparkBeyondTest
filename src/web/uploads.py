from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from pathlib import Path
from fastapi import FastAPI, Request, UploadFile, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
import aiofiles
import os
from fastapi.templating import Jinja2Templates
from pathlib import Path
from services import search

router = APIRouter(prefix = "/uploads")

top = Path(__file__).resolve().parent.parent
template_dir = f"{top}/template"
template_obj = Jinja2Templates(directory=template_dir)

page_element = '''
    <form action='/uploads' enctype='multipart/form-data' method='post'>
        <input name='file' type='file'>
        <input type='submit'>
    </form>
'''

@router.get("/")
def top(request: Request):

    return template_obj.TemplateResponse("layout.html",
        {   "request": request,
            "page_element": page_element})

@router.post('/')
async def post_upload(file: UploadFile):
    try:
        contents = await file.read()
        
        search.wordsearch_service().save_document_words(file.filename, contents)
    except Exception as e :
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='There was an error uploading the file',
        )
    finally:
        await file.close()

    return RedirectResponse(url="/uploads/", status_code=status.HTTP_303_SEE_OTHER)
