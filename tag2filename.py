# conding: utf-8

import glob
import os
import sys
from os import path

from mutagen.mp4 import MP4

SUFFIX = '.m4a'

def find_all_files( directory ):
    for root, dirs, files in os.walk( directory ):
        yield root
        for file in files:
            yield os.path.join( root, file )

input_dir = sys.argv[1]
input_dir = path.abspath( input_dir )
file_list = find_all_files( input_dir )

for i in file_list:
    if( i.endswith( SUFFIX ) ):
        mp4       = MP4( i )
        tags      = mp4.tags
        track_num = tags[ 'trkn' ][ 0 ]
        new_name  = "track_%02d%s" % ( track_num[ 0 ], SUFFIX )
        dir_name  = path.dirname( i )
        new_path  = path.join( dir_name, new_name )
        os.rename( src=i, dst=new_path )
        print( "{src} -> {dst}".format( src=i, dst=new_path ) )
