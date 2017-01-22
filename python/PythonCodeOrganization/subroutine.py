'''
please be cared about value pass and ref pass
'''
def basic_op(a,b):
    return a+b,a-b,a*b,a/b

def abs(a):
    a[0] = a[0] + 1
    return a

if __name__ == "__main__":
    print basic_op(7,8)
    b=[1,2,3]
    print b
    print abs(b)
    print b
