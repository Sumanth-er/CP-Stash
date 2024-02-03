gst = 0
total = 0
while 1:

    p = input('Enter amount')
    if p == 'exit':
        break
    else:
        p = int(p)
    gst += (p / 100) * 18
    total += p

print('Total billl', total)
print('taxible gst', gst)
print('total payment', total + gst)
