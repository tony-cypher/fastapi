from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import JSONResponse, PlainTextResponse
from router import blog_get, blog_post, user, article, product
from db import models
from db.database import engine
from exceptions import StoryException
# uvicorn main:app --reload

app = FastAPI()
app.include_router(user.router)
app.include_router(blog_get.router)
app.include_router(blog_post.router)
app.include_router(article.router)
app.include_router(product.router)


@app.get('/')
def index():
    return {'message': 'Hello World!!'}

@app.exception_handler(StoryException)
def story_exception_handler(request: Request, exc: StoryException):
    return JSONResponse(
        status_code = 418,
        content = {'detail': exc.name}
    )
# intercepts all exceptions
# @app.exception_handler(HTTPException)
# def custom_handler(request: Request, exc: StoryException):
#     return PlainTextResponse(str(exc), status_code=status.HTTP_400_BAD_REQUEST)

# creates database if it does not exist
models.Base.metadata.create_all(engine)