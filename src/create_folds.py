import pandas as pd 
from sklearn import model_selection
import os 

if __name__ == "__main__":
    df = pd.read_csv("~/PycharmProjects/Categorical_Feature_Encoding_Challenge/input/train.csv")
    df['kfold'] = -1
    df = df.sample(frac=1).reset_index(drop = True)
    kf = model_selection.StratifiedKFold(n_splits=5, shuffle=False, random_state=42)

    for fold,(train_index,val_idx) in enumerate(kf.split(X = df,y=df.target.values)):
        print(len(train_index),len(val_idx))
        df.loc[val_idx,'kfold'] = fold

    df.to_csv("~/PycharmProjects/Categorical_Feature_Encoding_Challenge/input/train_folds.csv",index=False)