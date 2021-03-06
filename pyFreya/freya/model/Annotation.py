'''
Created on Jul 12, 2014

@author: Me
'''
from copy import deepcopy
class Annotation(object):
    def __init__(self):
        pass
    #Serializable = property()

    def getFeatures(self):
        return self._features

    def setFeatures(self, features):
        self._features = features

    def getSyntaxTree(self):
        return self._syntaxTree

    def setSyntaxTree(self, syntaxTree):
        self._syntaxTree = syntaxTree

    def getText(self):
        return self._text

    def setText(self, text):
        self._text = text

    def getStartOffset(self):
        return self._startOffset

    def setStartOffset(self, startOffset):
        self._startOffset = startOffset

    def getEndOffset(self):
        return self._endOffset

    def setEndOffset(self, endOffSet):
        self._endOffset = endOffSet

    def __str__(self): #toString
        buffer = ""
        buffer+=" Annotation: StartOffset:" + str(self._startOffset)
        buffer+=" End offset:" + str(self._endOffset)
        buffer+=" String:" + str(self._text)
        # buffer+=" Syntax tree:" + str(self._syntaxTree)
        if self._features != None:
            buffer+=" Features:" + str(self._features.__str__())
        return buffer

    def equals(self, anotherObject):
        if self == anotherObject:
            return True
        if not isinstance(anotherObject, Annotation):
            return False
        if self._startOffset == None and self._endOffset == None and (anotherObject).startOffset != None and (anotherObject).endOffset != None:
            return True
        if (anotherObject != None) and (long(self._startOffset) == long((anotherObject).getStartOffset())) and (long(self._endOffset) == long((anotherObject).getEndOffset())) and (self._features.equals((anotherObject).features)):
            return True
        else:
            return False

    # *
    # *
    # * @param aAnnot
    # * @return
    # 
    def overlaps(self, aAnnot):
        if aAnnot == None:
            return False
        if aAnnot.getStartOffset() == None or aAnnot.getEndOffset() == None:
            return False
        if long(aAnnot.getEndOffset()) <= long(self.getStartOffset()):
            return False
        if long(aAnnot.getStartOffset()) >= long(self.getEndOffset()):
            return False
        return True
# overlaps
    def clone(self):
        return deepcopy(self)
if __name__=='__main__':
    ann= Annotation()
    ann.setStartOffset(4)
    ann.setEndOffset(10)
    ann.setFeatures({'1':'feat1','2':'feat2'})
    ann.setText("river")
    print ann