class A:
       def __init__(self,a):
              self.a = a
       def __lt__(self,other):
             if(self.a<other.a):
                    return "object 1 is less than object 2"
             else:
                    return "obect 2 is less than object 1"
             
       def __eq__(self,other):
                if(self.a==other.a):
                        return "both objects are equal"
                else:
                        return "both objects are not equal" 
                
obj1 = A(2)
obj2 = A(3)
print( obj2 < obj1 )

obj3 = A(4)
obj4 = A(4)
print(obj3==obj4)