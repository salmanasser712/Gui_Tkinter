import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image
import os.path


class Stroke:
    def __init__(self):
        self.data = pd.read_csv("Data/healthcare-dataset-stroke-data.csv", na_values=['Unknown'])

    def load(self):
        self.plot()
        mydata = self.data
        mydata = self.dr(mydata)
        mydata = self.clean(mydata)
        mydata = self.encode(mydata)
        mydata = self.norm(mydata)
        mydata = self.target(mydata)
        return mydata

    def desc(self):
        return self.data.describe()
    def target(self, mydata):
        y = mydata['stroke']
        mydata.drop(['stroke'], axis=1, inplace=True)
        mydata['y'] = y
        return mydata

    def clean(self, mydata):
        mean_value = mydata['bmi'].mean()
        mydata['bmi'].fillna(value=mean_value, inplace=True)
        mode_value = mydata['smoking_status'].mode()[0]
        mydata['smoking_status'].fillna(value=mode_value, inplace=True)
        return mydata

    def encode(self, mydata):
        lis = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        mydata = pd.get_dummies(data=mydata, columns=lis)
        return mydata

    def dr(self, mydata):
        if 'id' in list(mydata):
            mydata.drop(['id'], axis=1, inplace=True)
        return mydata


    def norm(self, mydata):
        lis = ['age', 'avg_glucose_level', 'bmi']
        for name in lis:
            min = mydata[name].min()
            max = mydata[name].max()
            mydata[name] = (mydata[name] - min) / (max - min)
        return mydata

    def plot(self):
        if os.path.exists("plots/StrokePlot1.png"): return
        plt.rcParams["figure.figsize"] = [4.50, 3.50]
        plt.rcParams["figure.autolayout"] = True
        plt.figure()
        sns.swarmplot(data=self.data, x="stroke", y="age", hue='gender')
        plt.savefig("plots/StrokePlot1.png")
        plt.close()
        return

    def des(self):
        return self.data.describe()
