from base.PolicyMetaModel import PolicyMetaModelBase
from actions.PolicyMetaModel import PolicyMetaModelActions

class PolicyMetaModel(PolicyMetaModelBase, PolicyMetaModelActions):
    '''
    classdocs
    '''
    def __init__(self, policymeta=[]):
        '''
        Constructor
        @param policymeta: policymeta minOccurs=0 maxOccurs=unbounded
        @type policymeta: PolicyMeta
        '''
        PolicyMetaModelBase.__init__(self, policymeta=policymeta)
