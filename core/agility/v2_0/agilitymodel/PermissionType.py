from core.agility.v2_0.agilitymodel.base.PermissionType import PermissionTypeBase
from core.agility.v2_0.agilitymodel.actions.PermissionType import PermissionTypeActions

class PermissionType(PermissionTypeBase, PermissionTypeActions):
    '''
    classdocs
    '''
    def __init__(self, global_=None, displayName=None):
        '''
        Constructor
        @param global_: global_ minOccurs=0
        @type global_: boolean
        @param displayName: displayName minOccurs=0
        @type displayName: string
        '''
        PermissionTypeBase.__init__(self, global_=global_, displayName=displayName)
