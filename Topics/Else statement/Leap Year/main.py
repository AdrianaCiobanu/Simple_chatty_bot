# put your python code here
i = int(input())
if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
    print('Leap')
else:
    print('Ordinary')
