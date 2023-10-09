t = int(input())
nmb = set(range(1, t + 1))
psb = nmb

while True:
    gst = input()
    if gst == 'HELP':
        break

    gst = {int(x) for x in gst.split()}

    if len(psb & gst) > len(psb) / 2:
        print('YES')
        psb &= gst
    else:
        print('NO')
        psb &= nmb - gst
        
print(' '.join([str(x) for x in sorted(psb)]))
