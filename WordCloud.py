from tkinter import *
import nltk
from nltk import *
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

master = Tk()

OPTIONS = [
    "Little Women", "Harry Potter 2", "Oliver Twist"
]

files = {"Little Women":"littlewomen.txt", "Harry Potter 2":"hpc.txt", "Oliver Twist":"oliver.txt"}

variable = StringVar(master)
variable.set(OPTIONS[0])

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

L1 = Label(master, text="Minimum number of repititions:")
L1.pack( side = LEFT)
entry = Entry(master, bd =5, text="100")
entry.pack(side = RIGHT)


def click():
    print("value is:" + variable.get())
    file = files[variable.get()]
    f = open(file, "r")
    data = f.read()
    tokens = nltk.word_tokenize(data)
    text = pos_tag(tokens)
    lis = []
    for word, pos in text:
        # print(word, pos)
        if (pos == "NN" or pos == "NNS" or pos == "NNP" or pos == "NNPS"):
            lis.append(word)
    # print(lis)
    fdist = nltk.FreqDist(lis)
    # print(fdist.most_common(20))

    words = []

    if(entry.get() == ""):
        count = 100
    else:
        count = int(entry.get())
    for w, c in fdist.most_common(1000):
        if(c >= count):
            words.append(w)
    mask1 = np.array(Image.open("girl.jpg"))
    wc = wordcloud.WordCloud(height=500, width=500, background_color='white').generate(" ".join(words))
    plt.figure()
    plt.imshow(wc)
    plt.axis("off")
    plt.show()
    f.close()

button = Button(master, text="GO", command=click)
button.pack(side=RIGHT)

mainloop()