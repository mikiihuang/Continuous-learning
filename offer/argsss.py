def docoration(fun):
    def output(*args,**kwargs):
        print("what is going\n")
        return fun(*args,**kwargs)
    return output

@docoration
def task(i):
    print("in task"+str(i))
task(2)

@docoration
def endless(a,b):
    print(str(a)+"in end"+str(b))
endless("hui"," ghwdb")