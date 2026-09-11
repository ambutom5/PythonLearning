smallest = lambda x,y,z:min(x,y,z)
print(smallest(5,1,3))

lowest = lambda x,y,z:x if(x<y and x<z) else y if(y<x and y <z) else z
print(lowest(5,3,8))