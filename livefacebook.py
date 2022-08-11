import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image
import os.path

class Live:
    def __init__(self):
        self.data = pd.read_csv("Data/Live.csv")

    def load(self):
        self.plot1()
        mydata = self.data
        mydata = self.encode(mydata)
        mydata = self.dr(mydata)
        #mydata = self.norm(mydata)
        mydata = self.target(mydata)
        return mydata

    def target(self, mydata):
        y = mydata['status_type']
        mydata.drop(['status_type'], axis=1, inplace=True)
        mydata['y'] = y
        return mydata

    def norm(self, mydata):
        lis = ['num_reactions', 'num_comments', 'num_shares', 'num_likes', 'num_loves', 'num_wows', 'num_hahas', 'num_sads', 'num_angrys']
        for name in lis:
            min = mydata[name].min()
            max = mydata[name].max()
            mydata[name] = (mydata[name] - min) / (max - min)
        return mydata

    def encode(self, mydata):
        lis = {"video": 1, "photo": 2, "link": 3, "status": 4}
        mydata = mydata.replace({"status_type": lis})
        return mydata

    def dr(self, mydata):
        lis = ['Column1', 'Column2', 'Column3', 'Column4', 'status_id', 'status_published']
        mydata.drop(lis, axis=1, inplace=True)
        return mydata

    def desc(self):
        return self.data.describe()


    def plot1(self):
        if os.path.exists("plots/num_loves.png"): return
        plt.rcParams["figure.figsize"] = [3.50, 2.50]
        plt.rcParams["figure.autolayout"] = True
        plt.figure()
        sns.stripplot(data=self.data, x="status_type", y="num_loves")
        plt.savefig("plots/num_loves.png")
        plt.close()
        return
