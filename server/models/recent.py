from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import *

class Base(DeclarativeBase):
    pass

class Recents(Base):
    __tablename__ = "recent_posts"

    id = mapped_column(Integer, primary_key=True)
    title = mapped_column(String(128), nullable=False)
    link = mapped_column(String(128), nullable=False)

    def __init__(self, id, title, link):
        self.id = id
        self.title = title
        self.link = link

    def __repr__(self) -> str:
        return f"{self.id}::{self.title} is @ {self.link}"

def dict_from_recents(post):
    return {
        "id": int(post.id),
        "title": str(post.title),
        "link": str(post.link)
    }
