from fastapi import APIRouter, File, UploadFile
import aiofiles


router = APIRouter(
    prefix='/file',
    tags=['file']
)

@router.post('/file')
def get_file(file: bytes=File(...)):
    content = file.decode('utf-8')
    lines = content.split('\n')
    return {'lines': lines}

@router.post('/uploadfile')
async def get_upload_file(upload_file: UploadFile=File(...)):
    path = f"media/{upload_file.filename}"

    async with aiofiles.open(path, 'wb') as buffer:
        while chunk := await upload_file.read(1024):
            await buffer.write(chunk)

    return {
        'filename': path,
        'type': upload_file.content_type
    }