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

log_fp     = open( file=path.join( input_dir, "tag2filename_log.txt" ), mode='w' )
err_log_fp = open( file=path.join( input_dir, "tag2filename_err_log.txt" ), mode='w' )

try:
    for i in file_list:
        if( i.endswith( SUFFIX ) ):
            mp4       = MP4( i )
            tags      = mp4.tags
            track_num = tags[ 'trkn' ][ 0 ]
            disk_num  = (1,1)

            if( 'disk' in tags ):
                disk_num = tags[ 'disk' ]

            new_name  = "track_%02d_%02d%s" % ( disk_num[ 0 ], track_num[ 0 ], SUFFIX )

            dir_name  = path.dirname( i )
            new_path  = path.join( dir_name, new_name )

            try:
                os.rename( src=i, dst=new_path )
                print( "{src} -> {dst}".format( src=i, dst=new_path ), file=log_fp )
            except Exception as e:
                print( "Disc:{disc}, Track:{track}, Path={path}".format( disc=disk_num[0], track=track_num[ 0 ], path=i), file=err_log_fp )
finally:
    log_fp.close()
    err_log_fp.close()
