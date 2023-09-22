import os
import sys

def playlist(index,path,name):
    return str(index)+'*file*'+os.path.join(path,name)+'\n'+ \
        str(index) + '*title*'+name+'\n\n'

def search_all_file(path,filetype):
    playlists = []
    obj = os.scandir(path)
    for entry in obj:
        if entry.is_dir():
            playlists+=search_all_file(os.path.join(path,entry),filetype)
        elif entry.name.endswith(filetype):
            print(entry.name)
            playlists.append([path,entry.name])
    return playlists

def generate_playlists(path,filetype):
    filename = os.path.basename(path)
    f = open(path+filename+".dpl", "w", encoding="utf-8")
    f.write("DAUMPLAYLIST\n")
    f.write("playname="+filename)
    f.write("""
    playtime=0
    topindex=0
    saveplaypos=0
    """)

    playlists = search_all_file(path,filetype)
    playlists
    for index,[path,name] in enumerate(playlists):
        f.write(playlist(index+1,path,name))
    f.write("\n")
    f.close()

if __name__ == '__main__':
    argv = sys.argv[1:]
    path = os.path.abspath(".")
    filetype = ".mp4"
    if '-h' in argv:
        print("""python playlist.py \"filepath\" \"filetype\"
    default filepath is current directory
    defaule filetype is \".mp4\"""")
        sys.exit(0)
        
    paraments = [path,filetype]
    for i,arg in enumerate(argv):
        paraments[i] = arg
    print("path:",paraments[0])
    print("filetype:",paraments[1])
    generate_playlists(paraments[0],paraments[1])
