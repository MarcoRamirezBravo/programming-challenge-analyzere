import sys
if len(sys.argv) < 3 :
    print("Needs at least two argument")
    exit()
elif (float(sys.argv[1]) < 0) or (float(sys.argv[1]) > 1000000000.0):
    print("Threshold have to be a number between 0.0 and 1,000,000,000.0")
    exit()
elif (float(sys.argv[2]) < 0) or (float(sys.argv[2]) > 1000000000.0):
    print('Limit have to be a number between 0.0 and 1,000,000,000.0')
    exit()
threshold = float(sys.argv[1])
limit = float(sys.argv[2])
print('Enter/Paste Input. Press Enter without typing any value when done.')
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    if(line != ''):
        contents.append(float(line))
    elif line == '':
        break
total = 0
pos = 0
flag = 0
for each in contents:
    if each<threshold:
        each=0.0
    if each>=threshold:
        each=each-threshold
    total_temp = total
    total+=each
    if total>limit and flag==0:
        each= limit-total_temp
        flag=1
    elif total>limit and flag==1:
        each = 0.0
    contents[pos] = each
    pos=pos+1
    print(each)
print(sum(contents))




