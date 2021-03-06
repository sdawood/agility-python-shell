from base.StoreProductAdapterItem import StoreProductAdapterItemBase
from actions.StoreProductAdapterItem import StoreProductAdapterItemActions

class StoreProductAdapterItem(StoreProductAdapterItemBase, StoreProductAdapterItemActions):
    '''
    classdocs
    '''
    def __init__(self, resource=[], description='', link=[], type='', id=None, name=''):
        '''
        Constructor
        @param resource: resource minOccurs=0 maxOccurs=unbounded
        @type resource: StoreResource
        @param description: description
        @type description: string
        @param link: link minOccurs=0 maxOccurs=unbounded
        @type link: Link
        @param type: type
        @type type: string
        @param id: id
        @type id: int
        @param name: name
        @type name: string
        '''
        StoreProductAdapterItemBase.__init__(self, resource=resource, description=description, link=link, type=type, id=id, name=name)
