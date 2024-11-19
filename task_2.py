n='Artem Dmitrenko'
upper=[ord(i) for i in '_'.join(n).upper()]
lower=[ord(i) for i in '_'.join(n).lower()]
r=upper+lower
print(max(r),min(r))