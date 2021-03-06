from core.agility.common.AgilityModelBase import AgilityModelBase


class FileSystemDeviceBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, device=None, cloudtype=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'device': {'type': 'string', 'name': 'device', 'minOccurs': '0', 'native': True}, 'cloudType': {'type': 'Link', 'name': 'cloudtype', 'minOccurs': '0', 'native': False}})
        self.device = device
        self.cloudtype = cloudtype 
