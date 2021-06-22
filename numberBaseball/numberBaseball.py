#숫자 야구
import random

print("숫자 야구 게임 \n")
print("중복되지 않는 임의의 1에서 9까지의 숫자를 자리에 맞게 맞추시면 됩니다. \n")

last_num = list()
baseball = random.randint(0, 9)
game_quit = 0 #자동 종료 방지
play_range = input("플레이 할 자릿수(1 ~ 9)를 입력해주세요: ")

def scale(x):
    while x == 0 or int(x) > 10:
        x = input("플레이 할 자릿수(1 ~ 9)를 입력해주세요: ")
        if x != 0 and int(x) < 10:
            return x 
            break
        else:
            continue #왜 자꾸 else가 먹통인데?? 
                         
scale(play_range)


for i in range(int(play_range)): #입력받은 자릿수 만큼 리스트 생성 
    while baseball in last_num:
        #while은 True일 때만 수행. 만약 임의의 숫자가 이미 리스트에 있을 시에는 다시 수행 (중복 없음) 
        baseball = random.randint(0, 9)
    last_num.append(baseball) 

st_cnt = 0 #strike
b_cnt = 0 #ball
turn_cnt = 0 #turn count

#print(last_num)


while st_cnt < int(play_range):
    total_input = input("\n띄어쓰기를 사용해 숫자 입력 : ") #숫자는 띄어쓰기로 구분
    total_input = total_input.split(' ') #split을 통해 받은 total_input은 str형태

    
    # ... 구문오류. 더 공부하고 수정해보자.... 
    #for i in range(1, len(total_input)):
        #if total_input != [''] or total_input[2i - 1] == chr(32) or (total_input[2i - 2] > chr(47) and total_input[2i - 2] < chr(58)): break 
        #else: continue


    #문자입력 또는 띄어쓰기가 제대로 되지 않았을 경우 방지하는 방법 없을까? 
    
    if total_input != ['']: #실수로 enter 눌렀을 경우 방지 
        pass
    else: continue 

 
    for i in range(int(play_range)):
        for j in range(int(play_range)):
            if last_num[i] == int(total_input[j]) and i == j:
                st_cnt += 1
            elif last_num[i] == int(total_input[j]) and i != j: 
                b_cnt += 1

    turn_cnt += 1

    if st_cnt == 0 and b_cnt == 0:
        print("Out!")
        continue
      
    print("strike: ", st_cnt, "ball: ", b_cnt)

    if st_cnt == int(play_range):
        print("Homerun!! ", turn_cnt, "번 만에 정답을 맞추셨습니다. \n")
        break

    st_cnt = 0 #strike, ball 개수 초기화
    b_cnt = 0
    
game_quit = input("Enter를 누르면 종료됩니다. \n")
  
