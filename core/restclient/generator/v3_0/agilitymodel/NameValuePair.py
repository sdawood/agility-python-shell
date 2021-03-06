from base.NameValuePair import NameValuePairBase
from actions.NameValuePair import NameValuePairActions

class NameValuePair(NameValuePairBase, NameValuePairActions):
    '''
    classdocs
    '''
    def __init__(self, id=None, value=None, name=''):
        '''
        Constructor
        @param id: id minOccurs=0
        @type id: int
        @param value: value minOccurs=0
        @type value: string
        @param name: name
        @type name: string
        '''
        NameValuePairBase.__init__(self, id=id, value=value, name=name)
