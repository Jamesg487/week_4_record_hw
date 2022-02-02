import pdb
from models.album import Album
from models.artist import Artist


import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Pink Floyd", 1973)
artist_repository.save(artist_1)
artist_2 = Artist("Megadeath", 1983)
artist_repository.save(artist_2)

album_1 = ("Atomic Heart Mother", "prog", artist_1)
album_repository.save(album_1)

# artist_repository.select(1)

pdb.set_trace()