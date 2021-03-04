a = []

for j in range(10):
    for i in range(1,11):
        a.append(i)

w = []
for k in range(1,11):
    w.append(k)

print(a)
print(w)

b = min(a)
print(b)

c = max(a)
print(c)

ax = sum(a) / len(a)
print(ax)

wx = sum(w) / len(w)
print(wx)

regions= {
    'a': min(min(a), 10),
    'b': min(sum(a)/len(a), 10),
    'c': sum(a)/len(a),
}
print(regions)
print(type(regions))

print(regions.keys())
print(regions['a'])
'''
for f in range(-20, 20):
    scan_front.append(scan.ranges[f])
front = sum(scan_front) / len(scan_front)
0.5 => 26cm
0.4 => 21cm
0.3 => 17cm
0.2 => 10cm

for fl in range(20, 75):
    scan_fleft.append(scan.ranges[fl])
fleft = sum(scan_fleft) / len(scan_fleft)
0.5 => 13cm
0.4 => 11cm
0.3 => 9cm
0.2 => 8cm

for l in range(75, 106):
    scan_left.append(scan.ranges[l])
left = sum(scan_left) / len(scan_left)
0.5 => 26cm
0.4 => 23cm
0.3 => 19cm
0.2 => 10cm

for fr in range(-75, -20):
    scan_fright.append(scan.ranges[fr])
fright = sum(scan_fright) / len(scan_fright)
0.5 => 15cm
0.4 => 10cm
0.3 => 5cm
0.2 => 2cm

for r in range(-105, -75):
    scan_right.append(scan.ranges[r])
right = sum(scan_right) / len(scan_right)
0.5 => 33cm
0.4 => 27cm
0.3 => 20cm
0.2 => 10cm

'''