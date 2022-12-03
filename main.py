file_list = ['1.txt','2.txt','3.txt']
file_size = {}

for file_name in file_list:
    with open(file_name, 'rt') as f:
        file_size[file_name] = sum(1 for line in f)
print (file_size)

list = []
for file, size in file_size.items():
    list.append((size,file))
print(list)
list.sort()
print(list)

union_f = open('union_file.txt', 'at')
for size, file in list:
    with open(file, 'rt') as fr:
        union_f.write(f'{file} \n')
        union_f.write(f'{size} \n')
        union_f.write(f'{fr.read()} \n')
union_f.close()

with open('union_file.txt', 'rt') as f:
    print(f.read())

