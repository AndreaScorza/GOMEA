'''from tqdm import tqdm
import time

pbar = tqdm(total=1000000)
for i in range(1000000):
    print(i)
    pbar.update(1)
pbar.close()

startTime = time.time()
for x in tqdm(range(0, 100)):
    time.sleep(0.01)
endTime = time.time()

tempo = round(endTime-startTime,2)
print("total amount of time: ", tempo)
'''

'''def add(x):
    return x+0.1
a = [0.1,0.2,0.3,0.4]

print(a)
for sol in a:
    sol = add(sol)

for x in range(0, len(a)):
    a[x] = add(a[x])

print(a)'''

pop = [[1], [2], [3], [4]]

print(type(pop[0]))
print(3 in pop)