n=int(input('N?'))
u=int(input('Primeiro termo?'))
r=int(input('Razão?'))
t0=u
t1=t0+r
print('{}->{}'.format(t0, t1), end='')
index=2
while index<=n:
    t2=t1+r
    print('->{}'.format(t2),end='')
    t0=t1
    t1=t2
    index+=1


