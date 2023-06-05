from app.models.posts.post_model import Genre,PostGenres,Post
from app.models.basemodel import db_connection,db
from app.queries.genres import create_genre,delete_genre
from app.queries.posts import create_post,get_all_films,get_film_by_id,delete_post
from app.schemas.posts import PostCreateSchema
from app.routes.posts import router
from fastapi import FastAPI
from fastapi_cache import FastAPICache
@db
def create_tables():
    db_connection.create_tables([Genre,Post,PostGenres])

create_tables()

app = FastAPI()

app.include_router(router)

# create_genre('Детектив')
# create_genre('Ужасы')
# # delete_genre('Детектив')
# print(get_genres())
# create_post('Пила','Очень страшно','1997','Америка',['Детектив','Ужасы'])
# create_post('Шерлок','Ничего не понятно','2012','Британия',['Детектив'])

# print(get_all_films())
# print(get_film_by_id(1))
# delete_post(1, 'Детектив')

# print(get_film_by_id(1))
# from datetime import date
# create_post(PostCreateSchema(title='Batman',description='Фильм про царя ночи',year=date(2015,1,1),country='USA',genre=['Детектив','Ужасы']))