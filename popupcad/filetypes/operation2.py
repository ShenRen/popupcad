# -*- coding: utf-8 -*-
"""
Written by Daniel M. Aukes.
Email: danaukes<at>seas.harvard.edu.
Please see LICENSE.txt for full license.
"""

from popupcad.algorithms.acyclicdirectedgraph import Node
from popupcad.filetypes.userdata import UserData
from popupcad.filetypes.classtools import ClassTools
from popupcad.filetypes.operationoutput import OperationOutput

         
class Operation2(Node,UserData,ClassTools):
    name = 'Operation'
    attr_init = tuple()
    attr_init_k = tuple()
    attr_copy = tuple()
    
    attr_ref = tuple()
    attr_refs = tuple()

    def __init__(self):
        Node.__init__(self)
        UserData.__init__(self)

    def editdata(self):
        try:
            del self.output
        except AttributeError:
            pass
        
    def parentrefs(self):
        return []

    def subdesignrefs(self):
        return []

    def sketchrefs(self):
        return []

    def replacerefs(self,refold,refnew):
        for attr in self.attr_ref:
            if getattr(self,attr)==refold:
                setattr(self,attr,refnew)
        for attr in self.attr_refs:
            list1 = getattr(self,attr)==refold
            while refold in list1:
                ii = list1.index(refold)
                list1[ii]=refnew

    def copy(self):
        newop = self.init_copy(self.attr_init,self.attr_init_k)
        newop.copyattrs(self,self.attr_copy)
        return newop
    
    def getoutputref(self):
        try:
            return self._outputref
        except AttributeError:
            self._outputref = 0
            return self._outputref

    def generate(self,design):
        result = self.operate(design)
        output = OperationOutput(result,'default',self)
        self.output = [output]

    @classmethod
    def new(cls,parent,design,currentop,newsignal):
        dialog = cls.buildnewdialog(design,currentop)
        if dialog.exec_()==dialog.Accepted:
            operation = cls(*dialog.acceptdata())
            newsignal.emit(operation)

    def edit(self,parent,design,editedsignal):
        dialog = self.buildeditdialog(design)
        if dialog.exec_()==dialog.Accepted:
            self.editdata(*dialog.acceptdata())
            editedsignal.emit(self)        
     
