foo = [1, 2, 3, 4, 5]
bar = [24, 52, 13, 27]

from package import list_ops, list_ops as lo

goo = list_ops.add(foo, bar)
print(("{} + {} = {}".format(foo, bar, goo)))
print(f"{foo} + {bar} = {goo}")

goo = list_ops.multiply(list_ops.spam, list_ops.ham)
print(("{} + {} = {}".format(list_ops.spam, list_ops.ham, goo)))
print(f"{list_ops.spam} * {list_ops.ham} = {goo}")

print("list_ops.spam: {list_ops.spam}")
# => list_ops.spam: [51, 23]

try:
    print("list_ops.eggs: {}".format(list_ops.eggs))
except Exception as e:
    print(e)


print("\n")
goo = lo.subtract(foo, bar)
print("{} - {} = {}".format(foo, bar, goo))
goo = lo.divide(bar, foo)
print("{} / {} = {}".format(bar, foo, goo))


print("\n")
from package.list_ops import add, subtract, spam
goo = add(foo, bar)
print(f"{foo} + {bar} = {goo}")
goo = subtract(bar, foo)
print(f"{bar} - {foo} = {goo}")
print(f"spam = {spam}")