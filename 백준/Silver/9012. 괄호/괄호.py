T = int(input())

for t in range(T):
    cnt = 0
    ps = str(input())
    if ps.count("(") != ps.count(")"):
        print("NO")
    
    else:
        for i in range(len(ps)):
            if ps[i] == "(":
                cnt += 1
            
            elif ps[i] == ")":
                cnt -= 1

            if cnt < 0:
                print("NO")
                break
            
            if i == (len(ps) - 1) and cnt == 0:
                print("YES")