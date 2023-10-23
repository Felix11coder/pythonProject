jina = 'python exception'

for j in jina:
    if (j != 1):
        print(j)

x = ['python', 'exception', 'try and except']

try:
    for i in range(4):
        print(f'The index and the elements from the list is {i, x[i]}')

except:
    print("Index out of range")
