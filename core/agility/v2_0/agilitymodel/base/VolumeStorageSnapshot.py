from core.agility.v2_0.agilitymodel.base.Item import ItemBase

class VolumeStorageSnapshotBase(ItemBase):
    '''
    classdocs
    '''
    def __init__(self, status=None, storage=None, volume=None, storeageSnapshots=list(), progress=None, snapshotId=None, cloud=None):
        ItemBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'status': {'type': 'string', 'name': 'status', 'minOccurs': '0', 'native': True}, 'storage': {'type': 'Link', 'name': 'storage', 'minOccurs': '0', 'native': False}, 'volume': {'type': 'Link', 'name': 'volume', 'minOccurs': '0', 'native': False}, 'storeageSnapshots': {'maxOccurs': 'unbounded', 'type': 'Link', 'name': 'storeageSnapshots', 'minOccurs': '0', 'native': False}, 'progress': {'type': 'string', 'name': 'progress', 'minOccurs': '0', 'native': True}, 'snapshotId': {'type': 'string', 'name': 'snapshotId', 'minOccurs': '0', 'native': True}, 'cloud': {'type': 'Link', 'name': 'cloud', 'minOccurs': '0', 'native': False}})
        self.status = status
        self.storage = storage
        self.volume = volume
        self.storeageSnapshots = storeageSnapshots
        self.progress = progress
        self.snapshotId = snapshotId
        self.cloud = cloud 
