#Embedded file name: pynt/headers/WinIoCtl.py
from ctypes import Structure, Union
from ..types import BYTE

def CTL_CODE(DeviceType, Function, Method, Access):
    return DeviceType << 16 | Access << 14 | Function << 2 | Method


METHOD_BUFFERED = 0
FILE_DEVICE_FILE_SYSTEM = 9
FILE_ANY_ACCESS = 0
FILE_SPECIAL_ACCESS = FILE_ANY_ACCESS
FSCTL_SET_OBJECT_ID = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 38, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_GET_OBJECT_ID = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 39, METHOD_BUFFERED, FILE_ANY_ACCESS)
FSCTL_DELETE_OBJECT_ID = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 40, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_SET_OBJECT_ID_EXTENDED = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 47, METHOD_BUFFERED, FILE_SPECIAL_ACCESS)
FSCTL_CREATE_OR_GET_OBJECT_ID = CTL_CODE(FILE_DEVICE_FILE_SYSTEM, 48, METHOD_BUFFERED, FILE_ANY_ACCESS)

class _FILE_OBJECTID_BUFFER_INNER2(Structure):
    _fields_ = [('BirthVolumeId', BYTE * 16), ('BirthObjectId', BYTE * 16), ('DomainId', BYTE * 16)]


class _FILE_OBJECTID_BUFFER_INNER1(Union):
    _anonymous_ = ['a1']
    _fields_ = [('a1', _FILE_OBJECTID_BUFFER_INNER2), ('ExtendedInfo', BYTE * 48)]


class FILE_OBJECTID_BUFFER(Structure):
    _anonymous_ = ['_u']
    _fields_ = [('ObjectId', BYTE * 16), ('_u', _FILE_OBJECTID_BUFFER_INNER1)]
