f = open('test.log','w')
s = '你好'
f.write(s)
f.close()
f = open('test.log','r')
print(f.read())

