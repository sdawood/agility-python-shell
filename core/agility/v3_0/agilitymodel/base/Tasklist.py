from core.agility.common.AgilityModelBase import AgilityModelBase


class TasklistBase(AgilityModelBase):
    '''
    classdocs
    '''
    def __init__(self, task=[], name='', offset=None, totalcount=None, limit=None, parentid=None):
        AgilityModelBase.__init__(self)
        self._attrSpecs = getattr(self, '_attrSpecs', {})
        self._attrSpecs.update({'Task': {'maxOccurs': 'unbounded', 'type': 'Task', 'name': 'task', 'minOccurs': '0', 'native': False}, 'name': {'type': 'string', 'name': 'name', 'native': True}, 'offset': {'type': 'int', 'name': 'offset', 'native': True}, 'totalCount': {'type': 'int', 'name': 'totalcount', 'native': True}, 'limit': {'type': 'int', 'name': 'limit', 'native': True}, 'parentId': {'type': 'int', 'name': 'parentid', 'native': True}})
        self.task = task
        self.name = name
        self.offset = offset
        self.totalcount = totalcount
        self.limit = limit
        self.parentid = parentid 
