hour, minute = map(int, input().split())

minute -= 45

if minute < 0:
    minute += 60
    hour = (hour - 1) % 24

print(hour, minute)
