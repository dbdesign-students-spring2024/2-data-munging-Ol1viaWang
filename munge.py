# Place code below to do the munging part of this assignment.

files= open('data/raw_data.txt', 'r')
lines= files.readlines()
files.close()

index1=0
index2= len(lines)-1
for i in range(len(lines)):
    if lines[i].startswith('Year'):
        index1 = i
        break

for i in range(index1 + 1, len(lines)):
    if lines[i].strip().isdigit():
        index2 = i

headers ='Year,Jan,Feb,Mar,Apr,May,Jun,Jul,Aug,Sep,Oct,Nov,Dec\n'
cleaned_data = [headers]

for line in lines[index1 + 1: index2 + 1]:
    if line.strip() and not line.strip().startswith('Year'):
        parts= line.split()
        year= parts[0]
        temps= parts[1:-1]
        cleaned_line = [year]
        for temp in temps:
            if temp =='****':
                cleaned_temp = ''
            else:
                if temp.isdigit() or (temp.startswith('-') and temp[1:].isdigit()):
                    celsius_hundredths = int(temp)
                    celsius = celsius_hundredths / 100.0
                    fahrenheit = (celsius * 9.0 / 5.0)
                    cleaned_temp = format(fahrenheit, '.1f')
                else:
                    cleaned_temp= ''
            cleaned_line.append(cleaned_temp)
        cleaned_data.append(','.join(cleaned_line) + '\n')
files2= open('data/clean_data.csv', 'w')
files2.writelines(cleaned_data)
files2.close()