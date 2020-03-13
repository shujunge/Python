"""
vprof -c cmh yourcode.py --output-file profile.json
"""
import time


def fun1(a, b):
    print('fun1')
    print(a, b)
    time.sleep(1)

def fun2():
    print('fun2')
    time.sleep(1)

def fun3():
    print('fun3')
    time.sleep(2)

def fun4():
    print('fun4')
    x=[i for i in range(1000)]
    time.sleep(1)

def fun5():
    print('fun5')
    time.sleep(1)
    x=[i for i in range(2000)]
    fun4()

fun1('foo', 'bar')
fun2()
fun3()
fun5()
