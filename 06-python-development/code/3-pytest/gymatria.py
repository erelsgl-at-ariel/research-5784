# -*- coding: utf-8 -*
class Gymatria:

    _aleph_beth = None
    
    def __init__(self,expression:str) -> None:
        self._expr = expression
        self._expr_value = Gymatria.get_value(expression)
    
   
    @property
    def expr_value(self)->int:
        return self._expr_value
   
    @property
    def expr(self) -> str:
        return self._expr
   
    @property 
    def aleph_beth(self):
        return Gymatria.get_aleph_beth()
    
    def __add__(self , other) -> int:
        if type(other)== int or type(other)== float:
            return self.expr_value + int(other)
        return self.expr_value + other.expr_value

    def __sub__(self , other) -> int:
        if type(other)== int or type(other)== float:
            return abs(self.expr_value - int(other))
        return abs(self.expr_value - other.expr_value)
    
    def __mul__(self , other) -> int:
        if type(other)== int or type(other)== float:
            return abs(self.expr_value * int(other))
        return self.expr_value * other.expr_value
    
    def __str__(self) -> str:
        return f"{self.expr} בגימטריה זה: {self.expr_value}"
    
    def __repr__(self) -> str:
        return f"Gymatria({self.expr!r})"
    
    def __int__(self) -> int: 
        return self.expr_value
    
    def __float__(self) ->float:
        return float(self.expr_value)

    
    
    @classmethod
    def get_aleph_beth(cls):
        if cls._aleph_beth == None:
            cls._set_aleph_beth()
        return cls.aleph_beth

    @classmethod
    def get_value(cls,expression:str =None) -> int:
        if expression == None:
            raise TypeError('invalid type')
        aleph_beth = cls.get_aleph_beth()
        expr_value = 0
        for ot in expression:
            if ord('א') <= ord(ot) <= ord('ת'):
                expr_value += aleph_beth[ot]
        return expr_value
        
    @classmethod
    def ot_sofit(cls, ot: str)-> bool:
        cls.otiot_sofiot = ['ץ','ך','ף','ן','ם']
        if ot in cls.otiot_sofiot:
            return True
        return False
    
    
    @classmethod
    def _set_aleph_beth(cls) -> None:
        ot_num = ord('א')
        cls.aleph_beth={}
        val = 1
        for i in range(27):
            cls.aleph_beth[chr(ot_num+i)] = val
            if not cls.ot_sofit(chr(ot_num+i)):
                if 90 >= val >= 10:
                    val+=10
                elif val >= 100:
                    val+= 100 
                else: val+=1
