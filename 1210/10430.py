#https://www.acmicpc.net/problem/10430
#https://ooyoung.tistory.com/21
a,b,c = map(int, input().split())

print((a+b)%c)
print(((a%c) + (b%c))%c)

print((a*b)%c)
print(((a%c) * (b%c))%c)


print(1,2,3,4, sep="&&&")