#Imaan
#5/23/2023
#Most of this is taken from this Medium article : https://jhumms.medium.com/how-to-build-a-custom-bingo-board-with-python-dc22f570bccc

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.style as style
import numpy as np
import random
from matplotlib.backends.backend_pdf import PdfPages


pdf = PdfPages('Bingo.pdf')
plt.rcParams.update({'font.size': 22})
style.use('seaborn-poster')


def bingo ():
    terms = list(range(1, 76))  #range of numbers
    for t in range(1, 76, 1):
        if t == 1:
            random.shuffle(terms)
            terms.insert(12, "Free")
        else:
            terms.pop(12)
            random.shuffle(terms)
            terms.insert(12, "Free")

    rowlen = 5  # makes a 5x5 bingo board
    fig = plt.figure()
    ax = fig.gca()
    ax.set_xticks(np.arange(0, rowlen + 1))
    ax.set_yticks(np.arange(0, rowlen + 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])
    plt.gca().title.set_text("BINGO")
    plt.grid(color='black', linewidth=5)

    for i, number in enumerate(terms[:rowlen**2]):
        x = (i % rowlen) + 0.45 - len(str(number))/50
        y = int(i / rowlen) + 0.45
        ax.annotate(number, xy=(x, y), xytext=(x, y))
    pdf.savefig(fig)


for i in range(1,11): #how many pages of sheets
    bingo()

pdf.close()
matplotlib.pyplot.close()