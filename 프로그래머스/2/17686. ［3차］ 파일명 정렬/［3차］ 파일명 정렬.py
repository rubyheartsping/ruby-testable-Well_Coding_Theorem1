def solution(files):
    ord_dict = {}
    
    def head_extract(file):
        for i in range(len(file)):
            if 48 <= ord(file[i]) <= 57:
                return file[:i].lower()
        
    def tail_strip(file):
        count = 0
        for i in range(len(file)):
            if 48 <= ord(file[i]) <= 57:
                count += 1
            elif count != 0 and not 48 <= ord(file[i]) <= 57:
                return file[:i].lower()
        else:
            return file[:i+1].lower()
    
    def pad_number(file, head):
        number = []
        for i in range(len(file)):
            if 48 <= ord(file[i]) <= 57:
                number.append(file[i])
            elif number and (ord(file[i]) < 48 or ord(file[i]) > 57) or len(number) == 5:
                break 
        return (head + "0" * (5 - len(number)) + "".join(number)).lower()
    
    def preprocessing(file):
        head = head_extract(file)
        mod_file = pad_number(tail_strip(file), head)
        return (head, mod_file)
    
    for file in files:
        head, mod_file = preprocessing(file)
        if head not in ord_dict.keys():
            ord_dict[head] = {mod_file : [file]}
        else:
            if mod_file not in ord_dict[head].keys():
                ord_dict[head][mod_file] = [file]
            else:
                ord_dict[head][mod_file].append(file)
    ord_dict = dict(sorted(ord_dict.items()))
    
    answer = []
    for head in ord_dict.keys():
        ord_dict[head] = dict(sorted(ord_dict[head].items()))
        for header in ord_dict[head].keys():
            answer += ord_dict[head][header]
    print(ord_dict)
    return answer

    
 