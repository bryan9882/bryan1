total_people = int(input("請輸入0-100個人:"))
list = [0]*total_people

for i in range(total_people):
    list[i]=i+1
index=0
while total_people > 0 :
    index = (index +2) % len(list)
    list.pop(index)
    if len(list) ==1:
        print(f"最後剩下的是第{list[0]}順位") 
        break








