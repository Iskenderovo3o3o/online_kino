from app.queries.posts import (
    get_all_films,
    get_film_by_id,
    create_post
    )

from app.schemas.posts import PostCreateSchema

from fastapi import APIRouter

from fastapi_cashe import FastAPICache



router = APIRouter()

@router.get('/posts')
def get_films():
    return get_all_films()

@router.post('/create-post')
def create_film(film: PostCreateSchema):
    return create_post(film)



@router.get('/posts/{id}')
def get_films(id):
    return get_all_films(id)
