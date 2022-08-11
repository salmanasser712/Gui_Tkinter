
import math
import numpy as np

class Guss:

    def get_p(self, m, v, x):
        ans = math.sqrt(2 * math.pi * v)
        if ans == 0.0:
            return 0.0000000000000000000000000000000000000000000001
        ans = ans ** (-1)
        t = ((x - m) ** 2)
        ans = ans * np.exp((-1) * (t / (2 * v)))
        return ans

    def px(self, row, train):
        ls = list(train)
        ans0 = 0
        ans1 = 0
        i = 0
        for x in row:
            if i != 0:
                m = train.groupby('y')[ls[i]].mean()
                v = train.groupby('y')[ls[i]].var()
                ans0 = ans0 + np.log(self.get_p(m[0], v[0], x))
                ans1 = ans1 + np.log(self.get_p(m[1], v[1], x))
            i = i + 1

        return [ans0, ans1]

    def get_per_gus(self, X_test, X_train):
        temp = X_train['y'].value_counts()
        p_sur = temp[1] / len(X_train)
        p_nsur = temp[0] / len(X_train)

        per = [0] * len(X_test)
        i = 0
        temp = np.array(X_test)
        for row in temp:
            ans = self.px(row, X_train)
            p0 = ans[0] * p_nsur
            p1 = ans[1] * p_sur
            if p0 > p1:
                per[i] = 0
            else:
                per[i] = 1
            i = i + 1
        return per