class tag:
    def __init__(self, name: str, innerHBML: list = [], Id: str = None, Class: str = None, attribs: dict = {}):
        """Create an HBML tag.
        
        Arguments:
        name -- The name of the tag.
        innerHBML -- The tags inside of this tag. Strings are not parsed.
        attribs -- The attributes of the tag."""
        self.name = name
        self.attribs = attribs
        self.innerHBML = innerHBML.copy() # must copy the list to avoid a bug
        self.id = Id
        self.Class = Class

    def tostring(self):
        result = f'{self.name}'
        if self.id:
            result += f'#{self.id}'
        if self.Class:
            result += f'.{self.Class}'

        if len(self.attribs) > 0:
            result += '['
            for attrib in self.attribs:
                result += f'{attrib}="{self.attribs[attrib]}"'
            result += ']'

        if len(self.innerHBML) == 0: # Don't need brackets if there's nothing in them
            return result

        if len(self.innerHBML) == 1 and type(self.innerHBML[0]) == str: # The tag contains a single string
            result += f' {{ "{self.innerHBML[0]}" }}'
        else:
            result += ' {\n'
            for tag in self.innerHBML:
                result += '\t' + tag.tostring() + '\n'
            result += '}'
        return result