from base.Domain import DomainBase
from actions.Domain import DomainActions

class Domain(DomainBase, DomainActions):
    '''
    classdocs
    '''
    def __init__(self, users=list(), roles=list()):
        '''
        Constructor
        @param users: users minOccurs=0 maxOccurs=unbounded
        @type users: Link
        @param roles: roles minOccurs=0 maxOccurs=unbounded
        @type roles: Link
        '''
        DomainBase.__init__(self, users=users, roles=roles)
