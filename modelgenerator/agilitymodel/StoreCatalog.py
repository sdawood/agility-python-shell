from base.StoreCatalog import StoreCatalogBase
from actions.StoreCatalog import StoreCatalogActions

class StoreCatalog(StoreCatalogBase, StoreCatalogActions):
    '''
    classdocs
    '''
    def __init__(self, products=list()):
        '''
        Constructor
        @param products: products minOccurs=0 maxOccurs=unbounded
        @type products: Link
        '''
        StoreCatalogBase.__init__(self, products=products)
