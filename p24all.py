import sys, re

def fulltest(num):
    if len(num) == 1:
        if num[0] == 24:
            return True
    else:
        numlen = len(num)
        for i in range(numlen - 1):
            for j in range(i + 1, numlen):
                num2 = num[:i] + num[i + 1:j] + num[j + 1:]
                ni = num[i]
                nj = num[j]
                if fulltest(num2 + [ni + nj]): return True
                if ni > nj and fulltest(num2 + [ni - nj]): return True
                if nj > ni and fulltest(num2 + [nj - ni]): return True
                if fulltest(num2 + [ni * nj]): return True
                if nj != 0 and nj != 1 and fulltest(num2 + [ni / nj]): return True
                if ni != 0 and ni != 1 and fulltest(num2 + [nj / ni]): return True
    return False

def quicktest(a, b, c, d):
    return fulltest([a, b, c, d])

ok = 0
notok = 0
for a in range(1, 14):
    for b in range(a, 14):
        for c in range(b, 14):
            for d in range(c, 14):
                a2, b2, c2, d2 = float(a), float(b), float(c), float(d)
                if quicktest(a2, b2, c2, d2):
                    ok = ok + 1
                else:
                    notok = notok + 1
print("ok=", ok, ", notok=", notok)
