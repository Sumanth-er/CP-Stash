print('KLH shopping mall')
print('**************************')
m_dis = int(input('Enter discount for men clothes'))
w_dis = int(input('Enter discount for women clothes'))
k_dis = int(input('Enter discount for kids clothes'))
total = 0
total_d = 0
while 1:
    n = input('Enter item type 1:men 2:women 3:kids')
    if n == '1':
        p = int(input('Enter price'))
        total += p
        total_d += (p * m_dis / 100)
    elif n == '2':
        p = int(input('Enter price'))
        total += p
        total_d += (p * w_dis / 100)
    elif n == '3':
        p = int(input('Enter price'))
        total += p
        total_d += (p * k_dis / 100)
    else:
        break
print('****************************')
print('Total price before discount', total)
print('Total price after discount', total_d)
print('total amount',total-total_d)
