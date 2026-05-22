tst1 = 'abc'
tst2 = 'def'

def func1(txt):
 return txt.upper()

def func2(txt1, txt2):
 res = func1(txt1) + txt2 # Вызываем func1 для txt1, затем склеиваем с txt2
 print(res)

func2(func1(tst1), tst2) # Вызов func2 с результатом func1(tst1) и tst2
