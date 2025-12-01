def solution(s):
    if len(s) == 4 or len(s) == 6:
            quar = list(s)
            quar.sort(reverse = True)
            for x in quar:
                if x >= "0" and x <= "9":
                    a = True

                else:
                    a = False
                    break
                    
            return a
                
    else:
        return False
