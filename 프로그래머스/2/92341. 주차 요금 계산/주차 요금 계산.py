from math import ceil

def solution(fees, records):
    parking_dict = {}
    for record in records:
        record = record.split()
        time = int(record[0][:2]) * 60 + int(record[0][3:])
        number = int(record[1])
        state = record[2]
        
        if number not in parking_dict.keys():
            parking_dict[number] = {
                "in_time" : time,
                "spent" : 0,
                "state" : state
            } 
        else:
            if state == "IN":
                parking_dict[number]["in_time"] = time
                parking_dict[number]["state"] = state
            else:
                parking_dict[number]["spent"] += time - parking_dict[number]["in_time"]
                parking_dict[number]["state"] = state
    
    parking_dict_keys = sorted(list(parking_dict.keys()))
    answer = []
    for number in parking_dict_keys:
        if parking_dict[number]["state"] == "IN":
            parking_dict[number]["spent"] += 1439 - parking_dict[number]["in_time"]
        fee = fees[1] + ceil((parking_dict[number]["spent"] - fees[0]) / fees[2]) * fees[3] if parking_dict[number]["spent"] > fees[0] else fees[1]
        answer.append(fee)
    print(parking_dict)
    return answer

    
        
                
            
            
            