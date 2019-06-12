# Given the tuple below that represents the Imelda May album "More Mayhem", write
# code to print the album details, followed by a listing of all the tracks in the album.
#
# Indent the tracks by a single tab stop when printing them (remember that you can pass
# more than one item to the print function, separating them with a comma).

imelda = "More Mayhem", "Imelda May", 2011, ((1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"),
                                             (4, "Kentish Town Waltz"))

# challenge5
# unpacking the tuple by 3 variables and another tuple

album, artist, year, tracks = imelda
print("Album {}, that came out in {}, performed by {} containing these tracks".format(album, year, artist))
for track in tracks:
    print("\t{}".format(track))

# we can unpack it further by assigning track number & track title variables

album, artist, year, tracks = imelda
print("Album {}, that came out in {}, performed by {} containing these tracks".format(album, year, artist))
for track in tracks:
    trackNo, title = track
    print("\tTrack #{}, title: {}".format(trackNo, title))
