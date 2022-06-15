import numpy as np
from sklearn import tree, metrics

# Processing Class
from sklearn.model_selection import train_test_split

class Processing:
    # Dataset definition
    inputs = []
    target = []
    GData = []
    Final = 0

    def __init__(self, data, ref, Target="HeartDiseaseorAttack",verbose=False):
        target = data['HeartDiseaseorAttack']
        inputs = data.drop(columns=[Target])

        inputs=inputs.to_numpy()
        Processing.GData = [[1, 30, 1, 1, 2, 0, 0, 1, 3, 3, 3, 1, 15]]

        #print(target, type(target))

        I_Train, I_Test, G_Train, G_Test = train_test_split(inputs, target, test_size=0.3, random_state=1)

        G_Train = G_Train.astype('int')
        G_Test  = G_Test.astype('int')

        model = tree.DecisionTreeClassifier(criterion="entropy", max_depth=3)
        model = model.fit(I_Train, G_Train)

        G_pred = model.predict(I_Test)
        Perc = metrics.accuracy_score(G_Test, G_pred)
        Perc = round(Perc*100)

        new_GData = np.asarray(Processing.GData)

        Result = model.predict(new_GData)
        if verbose: print(Result)
        Processing.Final+=int(Result)
        if verbose: print(ref, "- Accuracy:", Perc, "Percent")