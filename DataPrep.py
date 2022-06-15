import pandas as pd
import random

class DataPrep:

    def __init__(self, DataSource, StartValue = -1, verbose=False, DropColumns=['HighChol','CholCheck','PhysActivity','AnyHealthcare','NoDocbcCost','DiffWalk','Education','Income']):
        print("Starting Data Randomization Service")
        self.verbose = verbose
        if self.verbose: print("grab file")
        self.df = pd.read_csv(DataSource)
        self.df.drop(DropColumns, axis=1, inplace=True)
        if self.verbose: print(self.df)
        if StartValue < 0: self.StartValue = random.randrange(7,len(self.df),1)
        print("Started Data Randomization Service")

    def NextSet(self, amount):
        ret = pd.DataFrame(columns=self.df.columns)

        for i in range(0, amount+1):
            if self.StartValue+amount > len(self.df):
                self.StartValue = (self.StartValue+amount)-len(self.df)

            entry = self.df.loc[[self.StartValue+i]]

            while random.random() > .45:
                if self.StartValue > len(self.df):
                    self.StartValue = 1

                self.StartValue += 1
                entry = self.df.loc[[self.StartValue+i]]

                if self.verbose: print(self.StartValue)

            ret = pd.concat([ret,entry], ignore_index=True, axis=0)

        print(self.StartValue)

        return ret
