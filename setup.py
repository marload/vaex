"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

import os
from distutils.sysconfig import get_python_inc, get_python_lib
import numpy
import py2app
from distutils.core import setup, Extension
numdir = os.path.dirname(numpy.__file__)

import sys 
sys.setrecursionlimit(10000)

APP = ["bin/medavaex"]
DATA_FILES = ['bin/explore-qualities', 'gaussian3d-1e4.hdf5', "settings.ini", "settings_classes.ini", "rave-test.hdf5", ["data", ["data/oldplanar_c15_md0.002_z0.1h_H4_0.5_nH01_vw5s_ml30_sM2e9-snap_400.hdf5"]]]
OPTIONS = {'argv_emulation': False, 'excludes':["scipy"], 'resources':['python/gavi/icons'], 'matplotlib_backends':'-'}



include_dirs = []
library_dirs = []
libraries = []
defines = []
extra_compile_args = []
include_dirs.append(os.path.join(get_python_inc(plat_specific=1), "numpy"))
include_dirs.append(os.path.join(numdir, "core", "include"))

extensions = [
	Extension("gavifast", ["src/gavi.cpp"],
                include_dirs=include_dirs,
                library_dirs=library_dirs,
                libraries=libraries,
                define_macros=defines,
                extra_compile_args=extra_compile_args
                )
]

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    includes=["mayavi", "gavi", "md5"],
    ext_modules=extensions,
    package_data={'gavi': ['gavi/icons/*.png']}
    #packages=["h5py"]
)


libs = [line.strip() for line in """
libLLVM-3.3.dylib
libQtGui.4.dylib
libQtCore.4.dylib
libcrypto.1.0.0.dylib
libssl.1.0.0.dylib
libpng15.15.dylib
libfreetype.6.dylib
""".strip().splitlines()]

libpath = "/Users/maartenbreddels/anaconda/lib"
targetdir = 'dist/medavaex.app/Contents/Resources/lib/'
for filename in libs:
	path = os.path.join(libpath, filename)
	cmd = "cp %s %s" % (path, targetdir)
	print cmd
	os.system(cmd)

libs = [line.strip() for line in """
libpng15.15.dylib
""".strip().splitlines()]
targetdir = 'dist/medavaex.app/Contents/Resources/'
for filename in libs:
	#path = os.path.join(libpath, filename)
	cmd = "cp %s %s" % (path, targetdir)
	print cmd
	os.system(cmd)
