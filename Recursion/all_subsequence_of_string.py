'''
simple choice of weather to include an element from ip string or exclude it.
'''
def fun(op, ip):

    if len(ip) == 0:
        if op=='':
            print("'null'")
        else:
            print(op)
        return
    fun(op, ip[1:])
    fun(op + ip[0], ip[1:])


op = ''
ip = 'abc'

fun(op, ip)
