slang = "Hello welcome to Cathay 60th year anniversary"
slang = slang.upper()
dic = {}

for i in slang:
    if i in dic:
        dic[i] +=1
    else:
        dic[i] = 1
to_del = " "
if to_del in dic:
    del dic[to_del]       
            
for i,j in dic.items():
    print(f"{i} {j}")








        
        
        
    


    
