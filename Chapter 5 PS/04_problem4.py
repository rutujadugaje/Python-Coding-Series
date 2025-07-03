# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?


s = set()
s.add(20)
s.add(20.0)
s.add('20')
print(s)    #{20, '20'}
print(len(s))   #2


b = set()
b.add(20)
b.add(20.5)
b.add('20')
print(b)    #{'20', 20, 20.5}
print(len(b))   #3


