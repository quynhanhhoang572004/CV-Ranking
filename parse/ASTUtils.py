from abc import ABC, abstractmethod, ABCMeta
from dataclasses import dataclass
from typing import List, Tuple

def printlist(lst,f=str,start="[",sepa=",",end="]"):
	return start + sepa.join(f(i) for i in lst) + end

class ASTNode(ABC):
	@abstractmethod
	def accept(self, visitor):
		pass
	
@dataclass
class Prog(ASTNode):
    command: ASTNode  
    
    def accept(self, visitor):
        return visitor.visit_program(self)

@dataclass
class ShowTop(ASTNode):
    number: int
    def accept(self, visitor):
        return visitor.visit_show_top(self)

@dataclass
class ShowConditional(ASTNode):
    field: str #"level", "tool",...
    values : List[str]  

    def accept(self, visitor):
        return visitor.visit_show_conditional(self)
    


