# test_model.py
import pandas as pd

def test_data_shape():
    df = pd.read_csv("./data/student_data.csv")
    assert df.shape[0] > 0
    assert "G3" in df.columns

def test_no_nulls():
    df = pd.read_csv("./data/student_data.csv")
    assert df.isnull().sum().sum() == 0

