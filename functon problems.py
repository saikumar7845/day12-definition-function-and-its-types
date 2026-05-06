num=9
def even_odd(num):    #function even or odd number
    if num%2==0:
        print(f"{num}is a even number")
    else:
        print(f"{num}is a odd number")
even_odd(num)
even_odd(124)


def even_odd(num,num_2): #required arguments its throw an error extra argument values has taken
    print(num+num_2)
even_odd(10,20) 

def even_odd(name="sai"): # default arguments
    print(f"hai {name}")
even_odd("satish")
even_odd("Kollu") 
even_odd("sai")

def even_odd(num_2,num_3,num): # key= value arguments
    print(num*num_2*num_3)
even_odd(num=9,num_2=10,num_3=30)


def even_odd(*name):  # variable arguments with =indexing
    print(name[0])
even_odd("satish","srikanth","jayanth","kranthi") 
