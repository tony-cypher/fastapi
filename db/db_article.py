from sqlalchemy.orm.session import Session
from schema import ArticleBase
from db.models import DbArticle


def create_article(db: Session, request: ArticleBase):
    new_article = DbArticle(
        title = request.title,
        content = request.content,
        published = request.published,
        user_id = request.creator_id
    )
    db.add(new_article)
    db.commit()
    db.refresh(new_article)
    return new_article
    pass

def get_article(db: Session, id: int):
    article = db.query(DbArticle).filter(DbArticle.id == id).first()
    # Handle errors
    return article