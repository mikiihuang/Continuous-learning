def test_args(x, y, *args):
    print(x, y, args)

def test_kwargs(x,**kwargs):
    print(x,kwargs)

def args_kwargs(*args,**kwargs):
    print("args:",args)
    print("kwargs:",kwargs)

print("---test *args------")
test_args(1,2,3,4,5)
print("---test *kwargs------")
test_kwargs(1,a=2,b=3,c=4)
print("---test *args and *kwargs------")
args_kwargs(1,2,a=2,b=3,c=4)