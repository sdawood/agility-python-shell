from core.agility.v2_0.agilitymodel.base.StoreCategory import StoreCategoryBase
from core.agility.v2_0.agilitymodel.actions.StoreCategory import StoreCategoryActions

class StoreCategory(StoreCategoryBase, StoreCategoryActions):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        
        '''
        StoreCategoryBase.__init__(self)
