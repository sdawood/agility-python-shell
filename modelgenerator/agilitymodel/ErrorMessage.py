from base.ErrorMessage import ErrorMessageBase
from actions.ErrorMessage import ErrorMessageActions

class ErrorMessage(ErrorMessageBase, ErrorMessageActions):
    '''
    classdocs
    '''
    def __init__(self, message='', code='', detail='', isError=False):
        '''
        Constructor
        @param message: message
        @type message: string
        @param code: code
        @type code: string
        @param detail: detail
        @type detail: string
        @param isError: isError
        @type isError: boolean
        '''
        ErrorMessageBase.__init__(self, message=message, code=code, detail=detail, isError=isError)
