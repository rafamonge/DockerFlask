import pandas as pd

class Model:

    def predict(self, a):
        return a + 3

    def predict_df(self, df):
        #return df.assign(BMI = lambda x:  x.Peso / x.Altura / x.Altura) 
        return df.assign(BMI = lambda x:  x.Peso * 2) 