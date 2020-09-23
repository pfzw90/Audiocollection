class Track:
  def __init__(self, trackname, tracklength):
    self.name = trackname
    self.length = tracklength
  def show(self):
    print(f'Name: \"{self.name}\" | Length: {self.length} minutes')

class Album: 
  def __init__(self, albumname, band):
    self.name = albumname
    self.band = band
    self.tracklist = []

  def get_tracks(self):
    print(f'{self.name}: ')
    for track in self.tracklist:
      track.show()
  
  def add_track(self, trackname, tracklength):
    self.tracklist.append(Track(trackname, tracklength))

  def get_duration(self):
    duration = 0
    for track in self.tracklist:
      duration += track.length
    return duration


def create_audio_collection():
  global album_a
  global album_b 
  album_a = Album('The album A', 'The band A')
  album_b = Album('The album B', 'The band B')


  album_a.add_track('The song one', 1)
  album_a.add_track('The song two', 2)
  album_a.add_track('The song three', 3)

  album_b.add_track('The song four', 4)
  album_b.add_track('The song five', 5)
  album_b.add_track('The song six', 6)

  album_a.get_tracks()
  album_b.get_tracks()

create_audio_collection()
print(f'Album A duration: {album_a.get_duration()} mins.')
print(f'Album B duration: {album_b.get_duration()} mins.')





