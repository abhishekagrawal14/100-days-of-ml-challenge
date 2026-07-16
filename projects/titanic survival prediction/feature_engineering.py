import pandas as pd

def add_features(df):
    df = df.copy()
    df.drop(['PassengerId', 'Ticket'], axis=1, inplace=True)
    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df.drop(columns=['SibSp', 'Parch'],  inplace=True)
    df['FamilyGroup'] = pd.cut(df['FamilySize'], bins=[0, 1, 3, 11], labels=['Alone', 'Small', 'Large'])
    df.drop('FamilySize', axis=1, inplace=True)
    df['FamilyGroup'] = df['FamilyGroup'].map({'Alone': 0, 'Small': 1, 'Large': 2}).astype(int)
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    df['Cabin'] = df['Cabin'].notna().astype(int)
    df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.', expand=False)
    df['Title'] = df['Title'].apply(lambda x: x if x in ['Mr', 'Miss', 'Mrs', 'Master'] else 'Rare')
    df.drop('Name', axis=1, inplace=True)
    return df
