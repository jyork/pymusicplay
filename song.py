import eyed3

class Song:
    title: str
    artist: str
    album: str
    track_num: int
    def __init__(self) -> None:
        self.title = ''
        pass
        
    def load_file(self, file: str):
        with eyed3.load("song.mp3") as audiofile:
            self.title = audiofile.tag.title
            self.artist = audiofile.tag.artist
            self.album = audiofile.tag.album
            self.track_num = audiofile.tag.track_num

    @property
    def title(self) -> str:
        return self.title

    @property
    def artist(self) -> str:
        return self.artist

    @property
    def album(self) -> str:
        return self.album

    @property
    def track_num(self) -> int:
        return self.track_num
