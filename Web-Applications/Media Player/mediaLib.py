import os
class Video:

    def __init__(self, path):
        self.title = self.extractTitel(path)
        self.path = path
        self.staticPath = self.getStaticPath(path)
        self.subs = self.getSubs(self.path)
        self.mediaPath = self.getMediaPath(self.staticPath)

    def extractTitel(self, path):
        path = os.path.normpath(path)
        dirs = path.split(os.sep)
        return dirs[len(dirs) - 1]
    


    def getSubs(self, path):
        path = str(path)
        subs = []
        dir = path + "/subs"
        if os.path.isdir(dir):
            for it in os.scandir(dir):
                if it.is_file():
                    sub = Subs(dir + "/" + it.name)
                    subs.append(sub)
        return subs
    
    def getStaticPath(self, path):
        path = path[7:]
        return str(path)

    def getMediaPath(self, path):
        for file in os.scandir("static/" + path):
            if file.name[:1] == "m":
                return path + "/" + file.name
           
class Subs:
    def __init__(self, path):
        self.path = path
        self.subName = self.extractSubName(path)
        self.staticPath = self.getStaticPath(path)

    def extractSubName(self, path):
        path = os.path.normpath(path)
        dirs = path.split(os.sep)
        file = dirs[len(dirs) - 1]
        name = file[:len(file) - 4]
        return name

    def getStaticPath(self, path):
        path = path[7:]
        return str(path)


class Library:

    def __init__(self):
        self.media = self.extractMedia()

    def searchFiles(self, dir="static/media/"):
        media = []
        for it in os.scandir(dir):
            if it.is_dir():
                media.append(it.path)
        return media

    def extractMedia(self):
        media = []
        for dir in self.searchFiles():
            video = Video(dir)
            media.append(video)
        return media

    def getMediaByName(self, name):
        for media in self.media:
            if media.title == name:
                return media

if __name__ == "__main__":
    lib = Library()