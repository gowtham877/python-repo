class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
song = ["Happy birthday to you"]
bye = ["Good bye"]
happy_bday = Song(song)
good_bye = Song(bye)
good_bye.sing_me_a_song()
happy_bday.sing_me_a_song()
