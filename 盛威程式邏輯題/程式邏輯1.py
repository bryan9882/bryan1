def switch(num):
    tens_digits = num //10
    digits = num %10
    switch_num = digits*10+tens_digits
    return switch_num
switch_score = []
for i in range(5):
    original_score = int(input("請輸入成績:"))
    switchs = switch(original_score)
    switch_score.append(switchs)    
print(switch_score)
