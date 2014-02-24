from base.FileSystemDevice import FileSystemDeviceBase
from actions.FileSystemDevice import FileSystemDeviceActions

class FileSystemDevice(FileSystemDeviceBase, FileSystemDeviceActions):
    '''
    classdocs
    '''
    def __init__(self, device=None, cloudType=None):
        '''
        Constructor
        @param device: device minOccurs=0
        @type device: string
        @param cloudType: cloudType minOccurs=0
        @type cloudType: Link
        '''
        FileSystemDeviceBase.__init__(self, device=device, cloudType=cloudType)
