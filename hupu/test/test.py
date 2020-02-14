def yield_test(n):  
    for i in range(n):  
        yield call(i)  
        print(i,"one")
    #做一些其它的事情      
    print("do something.")      
    print("end.")  

def call(i):  
    return i*2  

#使用for循环  
# for i in yield_test(1):
# #     print(i,"two")
for i in yield_test(2):
    print(i,"two")
