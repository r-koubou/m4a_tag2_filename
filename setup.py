# coding: utf-8

import platform
import app_info
from cx_Freeze import setup, Executable

VERSION             = app_info.VERSION
AUTHOR              = app_info.AUTHOR
MAIN_SCRIPT         = app_info.MAIN_SCRIPT
CREATE_EXECUTABLE   = True
EXECUTABLE_NAME     = app_info.EXECUTABLE_NAME
DESCRIPTION         = app_info.DESCRIPTION
URL                 = app_info.URL

options             = {}

executable = EXECUTABLE_NAME
if platform.system().lower().startswith( 'win' ):
    executable += ".exe"

exe = None
if( CREATE_EXECUTABLE ):
    exe = Executable(
        script          = MAIN_SCRIPT,
        base            = None,
        copyright       = AUTHOR,
        targetName      = executable
    )

setup( name             = EXECUTABLE_NAME,
       version          = VERSION,
       author           = AUTHOR,
       description      = DESCRIPTION,
       url              = URL,
       options          = options,
       executables      = [exe] if exe != None else [] )
