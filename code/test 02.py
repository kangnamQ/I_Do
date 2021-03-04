c = 0
b = 100
h = 0
r = 0
done = True
wer = False
while not wer and done:


    c += 1
    b -= 2.5
    h += 2
    r = h/10 + (100-b)

    if c >= 40:
        done = False

    print(c)
    print(b)
    print(h)
    print(r)
    print("")
