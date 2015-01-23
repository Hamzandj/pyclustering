'''

Structures for exchange between core and python implementation.

Implementation: Andrei Novikov (spb.andr@yandex.ru)

'''

import pyclustering.core as core;
import os;

from ctypes import Structure, c_uint, c_double, POINTER;
from sys import platform as _platform;

# Path to DLL.
PATH_DLL_CCORE_WIN64 = None;

if (_platform == "linux") or (_platform == "linux2"):
    PATH_DLL_CCORE_WIN64 = core.__path__[0] + os.sep + "x64" + os.sep + "linux" + os.sep + "ccore.so";
elif (_platform == "win32"):
    PATH_DLL_CCORE_WIN64 = core.__path__[0] + os.sep + "x64" + os.sep + "win" + os.sep + "ccore.dll";

# Structures that are required for exchaging with DLL.
class cluster_representation(Structure):
    "Decription of cluster in memory"
    " - unsigned int number_objects"
    " - unsigned int * cluster_representation"
    
    _fields_ = [("number_objects", c_uint), 
                ("pointer_objects", POINTER(c_uint))];
    
    
class clustering_result(Structure):
    "Description of result of clustering in memory"
    " - unsigned int number_clusters"
    " - cluster_representation * pointer_clusters"
    
    _fields_ = [("number_clusters", c_uint), 
                ("pointer_clusters", POINTER(cluster_representation))];


class data_representation(Structure):
    "Description of input data"
    " - unsigned int number_object"
    " - unsigned int dimension"
    " - double ** pointer_objects"
    
    _fields_ = [("number_objects", c_uint), 
                ("dimension", c_uint), 
                ("pointer_objects", POINTER(POINTER(c_double)))];


class dynamic_result(Structure):
    "Description of output dynamic in memory"
    " - unsigned int size_dynamic"
    " - unsigned int size_network"
    " - double * times"
    " - double ** dynamic"
    
    _fields_ = [("size_dynamic", c_uint), 
                ("size_network", c_uint),
                ("times", POINTER(c_double)),
                ("dynamic", POINTER(POINTER(c_double)))];