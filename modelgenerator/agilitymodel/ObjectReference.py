from base.ObjectReference import ObjectReferenceBase
from actions.ObjectReference import ObjectReferenceActions

class ObjectReference(ObjectReferenceBase, ObjectReferenceActions):
    '''
    classdocs
    '''
    def __init__(self, fieldName=None, fieldAssetTypeName=None):
        '''
        Constructor
        @param fieldName: fieldName minOccurs=0
        @type fieldName: string
        @param fieldAssetTypeName: fieldAssetTypeName minOccurs=0
        @type fieldAssetTypeName: string
        '''
        ObjectReferenceBase.__init__(self, fieldName=fieldName, fieldAssetTypeName=fieldAssetTypeName)
