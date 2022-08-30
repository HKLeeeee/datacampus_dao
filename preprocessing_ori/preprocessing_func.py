import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler, LabelEncoder


def preprocess_df(df, onehot_col=None, scaling_col=None, drop_col = None, labeling_col = None, scaling_func=MinMaxScaler) :
    """
    :param df: 사용할 데이터프레임
    :param onehot_col: default = None, 원핫인코딩할 컬럼 리스트
    :param scaling_col: default = None, 스케일링할 컬럼 리스트
    :param drop_col: default = None, 사용하지 않을 컬럼 리스트
    :param labeling_col: default = None, 라벨링이 필요한 컬럼 리스트
    :param scaling_func: 스케일링시 사용할 컬럼, MinMaxScaler or StandardScaler
    :return: 전처리 된 데이터 프레임
    """
    if drop_col is not None :
        df = df.drop(drop_col, axis=1)
    if onehot_col is not None:
        df = pd.get_dummies(df, colums=onehot_col)
    if scaling_col is not None :
        for c in scaling_col :
            scaler = scaling_func()
            scaler.fit(df[[c]])
            df[c] = scaler.transform(df[[c]])
    if labeling_col is not None :
        for c in labeling_col :
            encoder = LabelEncoder()
            encoder.fit(df[c])
            df[c] = encoder.transform(df[c])
    return df
