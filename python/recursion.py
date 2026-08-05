#recurtion function
def show(n):
    if (n==0):  #base case
        return
    print(n)
    show(n-1)

show(3)    #5 4 3 2 1 


   
