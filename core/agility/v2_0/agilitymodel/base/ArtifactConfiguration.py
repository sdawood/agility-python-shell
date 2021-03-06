from core.agility.common.AgilityModelBase import AgilityModelBase


class ArtifactConfigurationBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, runtimeBindings=list(), variables=list(), id=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'runtimeBindings': {'maxOccurs': 'unbounded', 'type': 'ArtifactRuntimeBinding', 'name': 'runtimeBindings', 'minOccurs': '0', 'native': False}, 'variables': {'maxOccurs': 'unbounded', 'type': 'AssetProperty', 'name': 'variables', 'minOccurs': '0', 'native': False}, 'id': {'type': 'int', 'name': 'id', 'native': True}})
        self.runtimeBindings = runtimeBindings
        self.variables = variables
        self.id = id 
