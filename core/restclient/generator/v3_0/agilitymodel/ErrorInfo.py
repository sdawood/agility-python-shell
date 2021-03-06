from base.ErrorInfo import ErrorInfoBase
from actions.ErrorInfo import ErrorInfoActions

class ErrorInfo(ErrorInfoBase, ErrorInfoActions):
    '''
    classdocs
    '''
    def __init__(self, message=None, level=None):
        '''
        Constructor
        @param message: message minOccurs=0
        @type message: string
        @param level: level minOccurs=0
        @type level: ErrorLevel
        '''
        ErrorInfoBase.__init__(self, message=message, level=level)
