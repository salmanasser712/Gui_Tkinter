import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image
import os.path

class Mobile:
    def __init__(self):
        self.data = pd.read_csv("Data/train_mobile.csv")

    def load(self):
        self.plot1()
        self.plot2()
        self.plot3()
        self.plot4()
        mydata = self.data
        y = mydata['price_range']
        mydata.drop(['price_range'], axis=1, inplace=True)
        mydata['y'] = y
        return mydata

    def ret_data(self):
        return self.data.head()

    def desc(self):
        lis = ['battery_power', 'clock_speed', 'int_memory', 'm_dep', 'ram', 'talk_time']
        return self.data[lis].describe()

    def plot1(self):
        if os.path.exists("plots/price_and_ram.png"): return
        #plt.rcParams["figure.figsize"] = [2.50, 2.50]
        plt.rcParams["figure.autolayout"] = True
        plt.figure(figsize=(3, 2))
        sns.jointplot(x='ram', y='price_range', data=self.data, color='red', kind='kde')
        plt.savefig("plots/price_and_ram.png")
        plt.close()
        return

    def plot2(self):
        if os.path.exists("plots/3G_supported.png"): return
        plt.rcParams["figure.figsize"] = [3.50, 2.50]
        plt.rcParams["figure.autolayout"] = True
        labels = ["3G-supported", 'Not supported']
        values = self.data['three_g'].value_counts().values
        fig1, ax1 = plt.subplots()
        ax1.pie(values, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.savefig("plots/3G_supported.png")
        plt.close()
        return

    def plot3(self):
        if os.path.exists("plots/4G_supported.png"): return
        plt.rcParams["figure.figsize"] = [3.00, 2.50]
        plt.rcParams["figure.autolayout"] = True
        labels4g = ["4G-supported", 'Not supported']
        values4g = self.data['four_g'].value_counts().values
        fig1, ax1 = plt.subplots()
        ax1.pie(values4g, labels=labels4g, autopct='%1.1f%%', shadow=True, startangle=90)
        plt.savefig('plots/4G_supported.png')
        plt.close()
        return

    def plot4(self):
        if os.path.exists("plots/box_plt.png"): return
        plt.rcParams["figure.figsize"] = [3.50, 2.50]
        plt.rcParams["figure.autolayout"] = True
        plt.figure()
        sns.boxplot(x="price_range", y="battery_power", data=self.data)
        plt.savefig("plots/box_plt.png")
        plt.close()
        return