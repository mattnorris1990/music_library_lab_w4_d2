from db.run_sql import run_sql
from models.album import Album

import repositories.artist_repository as artist_repository

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"

    values = [album.title, album.genre, album.artist.id]

    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def select_all():
    albums = [] 

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], artist, row['genre'], row['id'])
        albums.append(album)
    return albums

def select(id):
    album = None
    sql = "SELECT * FROM album WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        artist = artist_repository.select(result['artist_id'])
        album = Album(result['title'], artist, result['genre'], result['id'])
        return album

