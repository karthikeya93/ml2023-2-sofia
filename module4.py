number = int(input('Hello user, please enter a positive integer'))
num_list = []

for i in range(number):
    num_list.append(int(input(f'Enter the number {i+1} out of {number}')))

check_num = int(input('Enter a number to check'))

if check_num in num_list:
    print(num_list.index(check_num))
else:
    print(-1)