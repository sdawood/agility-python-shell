from AgilityModelBase import AgilityModelBase

class LdapGroupListBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, mappings=[]):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'mappings': {'maxOccurs': 'unbounded', 'type': 'LdapGroup', 'name': 'mappings', 'minOccurs': '0', 'native': False}})
        self.mappings = mappings 