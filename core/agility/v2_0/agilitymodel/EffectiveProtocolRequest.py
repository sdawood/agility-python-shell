from core.agility.v2_0.agilitymodel.base.EffectiveProtocolRequest import EffectiveProtocolRequestBase
from core.agility.v2_0.agilitymodel.actions.EffectiveProtocolRequest import EffectiveProtocolRequestActions

class EffectiveProtocolRequest(EffectiveProtocolRequestBase, EffectiveProtocolRequestActions):
    '''
    classdocs
    '''
    def __init__(self, item=None, policyId=list()):
        '''
        Constructor
        @param item: item minOccurs=0
        @type item: Link
        @param policyId: policyId minOccurs=0 maxOccurs=unbounded
        @type policyId: int
        '''
        EffectiveProtocolRequestBase.__init__(self, item=item, policyId=policyId)
