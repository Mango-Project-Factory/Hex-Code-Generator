from random import randint

longer = int(input('Longer: '))
digit = int(input('Digits: '))

codeList = []

rangeMax = int('F'*digit, 16)
for i in range(longer):
    num = str(hex(randint(0, rangeMax)).replace('0x', '')).zfill(digit)
    codeList.append(num)

code = '-'.join(codeList)

print(f'Verify Code is {code}')



# Function Version

def randomVerifyCode(longer:int, digit:int):
    return '-'.join([hex(randint(0, int('F'*digit, 16))).replace('0x', '') for i in range(longer)])