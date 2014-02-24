from base.PublishRequest import PublishRequestBase
from actions.PublishRequest import PublishRequestActions

class PublishRequest(PublishRequestBase, PublishRequestActions):
    '''
    classdocs
    '''
    def __init__(self, comment=None, keepSubAssetsLocation=None):
        '''
        Constructor
        @param comment: comment minOccurs=0
        @type comment: string
        @param keepSubAssetsLocation: keepSubAssetsLocation minOccurs=0
        @type keepSubAssetsLocation: boolean
        '''
        PublishRequestBase.__init__(self, comment=comment, keepSubAssetsLocation=keepSubAssetsLocation)
