from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist('Cher')
artist2 = Artist('Michael Jackson')
artist3 = Artist('Michael Bolton')
artist_repository.save(artist1)
artist_repository.save(artist2)
artist_repository.save(artist3)

album1 = Album('Believe', artist1, 'Pop')
album2 = Album('Thriller', artist2, 'Pop')
album3 = Album('Bad', artist2, 'Pop')
album4 = Album('Soul Provider', artist3, 'Soul')
album_repository.save(album1)
album_repository.save(album2)
album_repository.save(album3)
album_repository.save(album4)

# album_repository.delete_all()
# artist_repository.delete_all()

# artists = artist_repository.select_all()
# for artist in artists:
#     print(artist.__dict__)

# albums = album_repository.select_all()
# for album in albums:
#     print(album.__dict__)
    
# artist_albums = artist_repository.album(artist2)
# for album in artist_albums:
#     print(album.__dict__)

artist3.name = "Bloc Party"
artist_repository.update(artist3)

album4.title = "Silent Alarm"
album_repository.update(album4)

album_repository.delete(album4.id)
artist_repository.delete(artist3.id)
