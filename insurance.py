from dataclasses import dataclass
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image
import os.path

class Ins:
    def __init__(self):
        self.data = pd.read_csv("Data/insurance.csv")

    def load(self):
        self.plot1()
        self.plot2()
        mydata = self.data
        mydata = self.encode(mydata)
        mydata = self.target(mydata)
        return mydata

    def target(self, mydata):
        y = mydata['charges']
        mydata.drop(['charges'], axis=1, inplace=True)
        mydata['y'] = y
        return mydata

    def encode(self, mydata):
        mydata.sex.replace('male', 0, inplace=True)
        mydata.sex.replace('female', 1, inplace=True)

        mydata.smoker.replace('yes', 0, inplace=True)
        mydata.smoker.replace('no', 1, inplace=True)

        mydata.region.replace('southeast', 1, inplace=True)
        mydata.region.replace('northwest', 2, inplace=True)
        mydata.region.replace('northeast', 3, inplace=True)
        mydata.region.replace('southwest', 4, inplace=True)
        return mydata

    def desc(self):
        return self.data.describe()

    def plot1(self):
        if os.path.exists("plots/insur.png"): return
        #plt.rcParams["figure.figsize"] = [3.50, 2.50]
        plt.rcParams["figure.autolayout"] = True

        region = self.data['region'].value_counts()
        labels = region.index
        sizes = region.values
        plt.figure(figsize=(3,3))
        colors = sns.color_palette('pastel')
        plt.pie(sizes,labels=labels,autopct='%1.1f%%',
        shadow = True, colors = colors, startangle = 90)
        plt.savefig("plots/insur.png")
        plt.close()
        return

    def plot2(self):
        if os.path.exists("plots/smoker.png"): return
        plt.rcParams["figure.figsize"] = [3.50, 2.50]
        plt.rcParams["figure.autolayout"] = True

        labels=['Non-Smoker','Smoker']
        size = self.data['smoker'].value_counts()
        colors=['#9A32CD','#8DEEEE']
        explode=(0,0.1)
        plt.pie(size, labels = labels, colors = colors, explode = explode, autopct = '%1.0f%%', pctdistance=0.4, labeldistance=0.7)
        circle = plt.Circle( (0,0),0.6, color='white')
        p=plt.gcf()
        p.gca().add_artist(circle)
        plt.savefig("plots/smoker.png")
        plt.close()
        return