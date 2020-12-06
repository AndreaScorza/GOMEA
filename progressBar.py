from tqdm import tqdm
import time

'''pbar = tqdm(total=1000000)
for i in range(1000000):
    print(i)
    pbar.update(1)
pbar.close()
'''
startTime = time.time()
for x in tqdm(range(0, 100)):
    time.sleep(0.01)
endTime = time.time()

tempo = round(endTime-startTime,2)
print("total amount of time: ", tempo)