everything in python is an object
list, dictonary, set, and bytearray are mutable objects - 
       this means you can change the elements of the object

Others like strings, turple, int, frozenset, float, bool are immutable - 
           this means that although you might change where let say a points at, in 
	   a = 5, 
	   if you assign a to let's say
	   a += 1
	   this means that python will find where a is and take the object 5 and add 1 giving 6, 
	   it will then point a where 6 is

This is different when compared with C since C takes the stores the int in address and will change 
  what has been stored in that particular address hence mutating a


  THIS MAKES SENSE??
