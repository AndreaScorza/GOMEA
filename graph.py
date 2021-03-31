import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics

# running normal with the ordering of the random key in the decoding
#absolute
RUN1A = [[0, 3], [1, 4], [2, 3], [3, 4], [4, 4], [5, 4], [6, 5], [7, 4], [8, 6], [9, 5], [10, 5], [11, 5], [12, 4], [13, 5], [14, 5], [15, 5], [16, 5], [17, 5], [18, 6], [19, 5], [20, 5], [21, 6], [22, 6], [23, 6], [24, 5], [25, 6], [26, 6], [27, 6], [28, 6], [29, 6], [30, 6], [31, 6], [32, 6], [33, 6], [34, 6], [35, 6], [36, 7], [37, 6], [38, 7], [39, 7], [40, 7], [41, 7], [42, 7], [43, 7], [44, 7], [45, 7], [46, 8]]
RUN2A = [[0, 3], [1, 3], [2, 4], [3, 4], [4, 4], [5, 4], [6, 5], [7, 5], [8, 5], [9, 5], [10, 5], [11, 6], [12, 5], [13, 5], [14, 6], [15, 5], [16, 6], [17, 5], [18, 5], [19, 6], [20, 6], [21, 6], [22, 6], [23, 6], [24, 6], [25, 6], [26, 6], [27, 6], [28, 6], [29, 7], [30, 6], [31, 6], [32, 7], [33, 6], [34, 7], [35, 6], [36, 7], [37, 6], [38, 7], [39, 6], [40, 6], [41, 7], [42, 7], [43, 7], [44, 7], [45, 7], [46, 7], [47, 7], [48, 7], [49, 8]]
RUN3A = [[0, 3], [1, 3], [2, 3], [3, 4], [4, 4], [5, 4], [6, 4], [7, 5], [8, 5], [9, 5], [10, 5], [11, 5], [12, 5], [13, 5], [14, 6], [15, 5], [16, 5], [17, 6], [18, 5], [19, 5], [20, 5], [21, 5], [22, 5], [23, 6], [24, 6], [25, 6], [26, 6], [27, 6], [28, 6], [29, 6], [30, 6], [31, 7], [32, 7], [33, 6], [34, 7], [35, 7], [36, 7], [37, 6], [38, 7], [39, 7], [40, 7], [41, 6], [42, 7], [43, 7], [44, 7], [45, 7], [46, 7], [47, 7], [48, 8]]
RUN4A = [[0, 3], [1, 3], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 5], [9, 6], [10, 5], [11, 5], [12, 5], [13, 5], [14, 6], [15, 5], [16, 5], [17, 6], [18, 6], [19, 6], [20, 6], [21, 7], [22, 6], [23, 6], [24, 6], [25, 6], [26, 7], [27, 7], [28, 7], [29, 7], [30, 7], [31, 6], [32, 7], [33, 7], [34, 7], [35, 7], [36, 8]]
RUN5A = [[0, 3], [1, 3], [2, 3], [3, 4], [4, 4], [5, 5], [6, 5], [7, 5], [8, 5], [9, 4], [10, 4], [11, 5], [12, 5], [13, 5], [14, 5], [15, 5], [16, 5], [17, 5], [18, 7], [19, 6], [20, 6], [21, 6], [22, 6], [23, 6], [24, 7], [25, 7], [26, 7], [27, 7], [28, 7], [29, 7], [30, 7], [31, 8]]

#relative
RUN1B =
RUN2B =
RUN3B =
RUN4B =
RUN5B =

#JUST USING DELTA1

#JUST USING DELTA2


def sameLength(list):
    ln = len(list)
    score = list[ln - 1][-1:][0]
    while len(list) < 100:
        list.append([ln, score])
        ln += 1
    return list


RUN1A = sameLength(RUN1A)
RUN2A = sameLength(RUN2A)
RUN3A = sameLength(RUN3A)
RUN4A = sameLength(RUN4A)
RUN5A = sameLength(RUN5A)

def avgVect(a,b,c,d,e):
    avg = []
    for x in range(0, 100):
        avg.append((a[x][-1:][0] + b[x][-1:][0] + c[x][-1:][0] + d[x][-1:][0] + e[x][-1:][0]) / 5)
    return avg


def printAbsolute():
    df=pd.DataFrame({'x_values': [row[0] for row in RUN2A], 'y_values': avgVect(RUN1A, RUN2A, RUN3A, RUN4A, RUN5A) })
    plt.title("Absolute")
    plt.xlabel("Generation Number")
    plt.ylabel("Maximum number of correct subproblems")
    plt.ylim(0,8.3)
    plt.xlim(0, 100)
    plt.plot( 'x_values', 'y_values', data=df, color='skyblue')
    plt.grid()
    plt.savefig("Absolute.png")
    #plt.show()


def printRelative(a, b, c, d, e):
    df = pd.DataFrame({'x_values': [row[0] for row in RUN1A], 'y_values': avgVect(RUN1B, RUN2B, RUN3B, RUN4B, RUN5B)})
    plt.title("Relative")
    plt.xlabel("Generation Number")
    plt.ylabel("Maximum number of correct subproblems")
    plt.ylim(0,8.3)
    plt.xlim(0, 100)
    plt.plot('x_values', 'y_values', data=df, color='skyblue')
    plt.grid()
    #plt.savefig("Relative.png")
    plt.show()


#print(printAbsolute())
#print(printRelative())

'''
bisogna vedere solo con delta1 o solo con delta2
---

correggi che lultimo pezzo viene salvato nella lista
'''

