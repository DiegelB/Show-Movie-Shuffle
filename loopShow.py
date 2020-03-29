

import os, random

def main():
    a = showName()
    b = showName()
    c = showName()
    d = showName()
    e = showName()
    f = showName()

    os.system("vlc --fullscreen --play-and-exit '"+a+"';"+
              "vlc --fullscreen --play-and-exit '"+b+"';"+
              "vlc --fullscreen --play-and-exit '"+c+"';"+
              "vlc --fullscreen --play-and-exit '"+d+"';"+
              "vlc --fullscreen --play-and-exit '"+e+"';"+
              "vlc --fullscreen --play-and-exit '"+f+"';")


def showName():
    tvChoice = random.choice(os.listdir("/home/skelly/Ent/TvShows/"))
    if (tvChoice == "Singles"):
        tvChoice2 = random.choice(os.listdir("/home/skelly/Ent/TvShows/" + tvChoice + "/"))

        tvChoice2 = "/home/skelly/Ent/TvShows/" + tvChoice + "/" + tvChoice2
        return tvChoice2

    else:
        tvChoice2 = random.choice(os.listdir("/home/skelly/Ent/TvShows/" + tvChoice + "/"))
        tvChoice3 = random.choice(os.listdir("/home/skelly/Ent/TvShows/" + tvChoice + "/" + tvChoice2 + "/"))
        
        tvChoice3 = "/home/skelly/Ent/TvShows/" + tvChoice + "/" + tvChoice2 + "/" + tvChoice3
        return tvChoice3



main()
