# Problem1
import random
def Print_values(a,b,c):
    if type(a)==str or type(b)==str or type(c)==str:
        print(type(a),type(b),type(c))
        print ("请输入整数")
    else:
        if a>b:
            if b>c:       
                print(a,b,c)
            elif a>c: 
                print(a,c,b)
            else:        
                print(c,a,b)
        elif a>c:          
            print(b,a,c)
        elif b>c: 
            print(b,c,a)
        else:                   
            print(c,b,a)

for i in range(10):
  a = random.randint(1, 10)
  b=random.randint(1, 10)
  c=random.randint(1, 10)
  Print_values(a,b,c)
