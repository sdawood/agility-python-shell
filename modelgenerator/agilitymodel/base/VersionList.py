from AgilityModelBase import AgilityModelBase

class VersionListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, versions=list()):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'versions': {'maxOccurs': 'unbounded', 'type': 'AgilityVersion', 'name': 'versions', 'minOccurs': '0', 'native': False}})
        self.versions = versions 
