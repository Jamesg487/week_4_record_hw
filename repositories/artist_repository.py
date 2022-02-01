from db.run_sql import run_sql

from models.artist import Artist

def save(artist):
    sql = f"INSERT INTO artists (name, year_formed) VALUES (%s, %s)"
    values = [artist.name, artist.year_formed]
    run_sql(sql, values)
    # id = results[0]['id']
    # artist.id = id
    # return artist

def delete_all():
    sql = "DELETE  FROM artists"
    run_sql(sql)

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = Artist(result['name'], result['year_formed'], result['id'] )
    return artist