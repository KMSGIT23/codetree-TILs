import sys
input = sys.stdin.readline
def f(a, b):
    if b==0:
        return a
    return f(b, a%b)
if __name__=="__main__":
    n = int(input())
    a, b=map(int, input().split())
    c = f(a, b)
    for i in range(1, c + 1):
        if c % i == 0:
            print(i)