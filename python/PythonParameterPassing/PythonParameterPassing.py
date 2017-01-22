
def f(a,b,c):
    return a+b+c
def func_default(a,b,c=10):
    return a+b+c
def func_tuplepack(*name):
    print type(name)
    print name
def func_keywordpack(**dic):
    print type(dic)
    print dic
def func_mix(a,b,c=0,*args, **kw):
    print('a=',a,'b=', b, 'c=', c, 'args=', args, 'kw=', kw)

def SequencePass():
    print(f(1,2,3))
def KeywordPass():
    print(f(c=3,b=2,a=1))
def DefaultValue():
    print(func_default(3,2))
    print(func_default(3,2,1))
def PackagePass():
    func_tuplepack(1,4,6)
    func_tuplepack(5,6,7,1,2,3)
    func_tuplepack(*(10,20))
    func_keywordpack(a=1,b=2)
    func_keywordpack(a=1,b=2,c=5)
    func_keywordpack(**{'a':1,'b':2,'c':5})
def MixPass():
    func_mix(1,2,3,'a','b',x=99,y=88)
    func_mix(1,2,3,*('a','b'),**{'x':99, 'y':88})
    pass


if __name__ == "__main__":
    SequencePass()
    KeywordPass()
    DefaultValue()
    PackagePass()
    MixPass()

