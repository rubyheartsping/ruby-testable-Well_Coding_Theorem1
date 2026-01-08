import sys
input = sys.stdin.readline
N = int(input())

locations = [str(input().rstrip("\n")) for n in range(N)]
locations = sorted(locations, key = lambda x : int(x.split()[1]))
locations = sorted(locations, key = lambda x : int(x.split()[0]))
for location in locations:
    print(location)