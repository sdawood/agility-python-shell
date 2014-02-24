from base.VariableValueSet import VariableValueSetBase
from actions.VariableValueSet import VariableValueSetActions

class VariableValueSet(VariableValueSetBase, VariableValueSetActions):
    '''
    classdocs
    '''
    def __init__(self, value=list(), valueSource=None):
        '''
        Constructor
        @param value: value minOccurs=0 maxOccurs=unbounded
        @type value: AssetProperty
        @param valueSource: valueSource minOccurs=0
        @type valueSource: Asset
        '''
        VariableValueSetBase.__init__(self, value=value, valueSource=valueSource)
