from base.PropertyDefinitionGroup import PropertyDefinitionGroupBase
from actions.PropertyDefinitionGroup import PropertyDefinitionGroupActions

class PropertyDefinitionGroup(PropertyDefinitionGroupBase, PropertyDefinitionGroupActions):
    '''
    classdocs
    '''
    def __init__(self, derivedgroup=[], displayname=None, parent=None, propertydefinition=[]):
        '''
        Constructor
        @param derivedgroup: derivedgroup minOccurs=0 maxOccurs=unbounded
        @type derivedgroup: Link
        @param displayname: displayname minOccurs=0
        @type displayname: string
        @param parent: parent minOccurs=0
        @type parent: Link
        @param propertydefinition: propertydefinition minOccurs=0 maxOccurs=unbounded
        @type propertydefinition: PropertyDefinition
        '''
        PropertyDefinitionGroupBase.__init__(self, derivedgroup=derivedgroup, displayname=displayname, parent=parent, propertydefinition=propertydefinition)
