from random import randint

"""1"""
print('1:')
random_list: list[int] = [randint(1, 100) for _ in range(50)]
print(random_list)

print('a:')
print(list(filter(lambda num: num > 50, random_list)))

print('b:')
print(list(filter(lambda num: num % 7 == 0, random_list)))

print('c:')
print(list(filter(lambda num: 10 < num < 100, random_list)))

print('d:')
print(list(filter(lambda num: num % 10 == num // 10, random_list)))

print('e:')
print(list(filter(lambda num: num % 10 + num // 10 == 9, random_list)))

print('f:')
print(list(filter(lambda num: num > sum(random_list) / len(random_list), random_list)))

print('g:')
print(list(filter(lambda num: num > max(random_list) / 2, random_list)))
"""2"""
print('2.')
hw_list: list[str] = ["Grand Theft Auto V", "Fortnite", "Overwatch", "Dark Souls", "The Elder Scrolls V: Skyrim", ]
print('a:')
print(list(filter(lambda w: len(w) > 8, hw_list)))
print('b:')
print(list(filter(lambda w: w.upper().startswith('F'), hw_list)))
print('c:')
print(list(filter(lambda w: len(w.split()) == 2, hw_list)))
print('d:')
print(list(filter(lambda w: 'V' in w, hw_list)))
"""3"""
print('3:')
list_3: list[int] = [randint(-50, 50) for _ in range(20)]
print(list_3)
print('a:')
print(list(map(lambda x: x ** 3, list_3)))
print('b:')
print(list(map(lambda x: -x % -10 and x % 10, list_3)))
print('c:')
print(list(map(lambda x: x * 9 / 5 + 32, list_3)))
print('d:')
print(list(map(lambda x: "positive" if x > 0 else "negative", list_3)))
"""4"""
print('4:')
fruits: list[str] = ["Mango ", "Orange ", "Banana ", "Apple ", "Strawberry", "Pineapple", "Grapes", "Watermelon"]
print('a:')
print(list(map(lambda w: w[::-1], fruits)))
print('b:')
print(list(map(lambda w: w[0], fruits)))
print('c:')
print(list(map(lambda w: w.upper(), fruits)))
print('d:')
print(list(map(lambda w: w[len(w) // 2], fruits)))
print('e:')
print(list(map(lambda w: w + '!' if w.endswith('s') else w, fruits)))
"""5"""
print('5:')
# משמעות המילה - global בתוך פונקציה קוראת למספר שקבענו מחוץ לפונקציה ומשתמש בו.
# החיסרון בשימוש של global בפונקציה מצריך בבניית הערך הגלובלי בכל תוכנית מחדש כאשר קוראים לפונקצייה בתוכנית אחרת.

# x: int = 1
# def foo():
#    print(x)
#    x = 4
# foo()
# בגלל שה -X בתוך הפונקציה לא מוגדר,ה - X בתוכנית הוא גלובלי ולא כתוב בפונקפציה -global
