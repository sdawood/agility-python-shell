from core.agility.v2_0.agilitymodel.base.Asset import AssetBase

class TargetCloudBase(AssetBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, maxInstances=None, models=list(), template=None, stack=None, cloud=None):
        AssetBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'maxInstances': {'type': 'int', 'name': 'maxInstances', 'minOccurs': '0', 'native': True}, 'models': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'models', 'minOccurs': '0', 'native': False}, 'template': {'type': 'Link', 'name': 'template', 'minOccurs': '0', 'native': False}, 'stack': {'type': 'Link', 'name': 'stack', 'minOccurs': '0', 'native': False}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.maxInstances = maxInstances
        self.models = models
        self.template = template
        self.stack = stack
        self.cloud = cloud 
