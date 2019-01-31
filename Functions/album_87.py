#8-7/8-8, Python Crash Course, User Album

def make_album(artistName, albumTitle, numTracks= ""):
    """Returns a dictionary describing an album"""
    album = {"artist": artistName, "title": albumTitle}

    if numTracks:
        album["numTracks"] = numTracks

    return album

while True:
    print("\nPleas Describe the album (Enter 'q' at any time to exit):")
    name = input("Name of Album: ")
    if name == 'q':
        break
    
    artist = input("Name of Artist: ")
    if artist == 'q':
        break
    
    numOfTracks = input("Number of Tracks(optional): ")
    if numOfTracks == 'q':
        break

    album = make_album(artistName= artist,
                       albumTitle= name,
                       numTracks= numOfTracks)
    
    print("\nDictionary of Album: " + str(album))
