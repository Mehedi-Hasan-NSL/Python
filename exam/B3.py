

## see B3.docx file for the run instructions


## part1 

import sys
import os 


def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir, file)
        if os.path.isdir(d):
            yield d
            listdirs(d)

root_dir = os.path.dirname(os.path.abspath(__file__))
#print(os.listdir(root_dir))
for dir in listdirs(root_dir):
	if os.path.isdir(dir):
		sys.path.append(dir)

import musicplayer
from musicplayer import audio, bar, foo
from musicplayer.audio import read_audio





## part 2 

import sys
print(sys.path)
sys.path.append('..')
from ..musicplayer.audio import read_audio