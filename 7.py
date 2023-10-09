q = int(input())
numbers = set(range(1, q + 1))

psb = numbers
while True:
    gst = input()

    if gst == 'HELP':
        break
    gst = {int(x) for x in gst.split()}
    answer = input()


    if answer == 'YES':
        psb &= gst
    else:
        psb &= numbers - gst



print(' '.join([str(x) for x in sorted(psb)]))
