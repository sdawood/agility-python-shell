from AgilityModelBase import AgilityModelBase

class NetworkInterfaceListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, networkinterface=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'NetworkInterface': {'maxOccurs': 'unbounded', 'type': 'NetworkInterface', 'name': 'networkinterface', 'minOccurs': '0', 'native': False}})
        self.networkinterface = networkinterface 
