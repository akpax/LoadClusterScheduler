import pytest
import sys
import pandas as pd
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = Path(__file__).parent.parent.resolve()
sys.path.append(str(parent_dir))
print(__file__)
from main import format_data_for_training


file_path = "test_files/Pier Loads.xlsx"
df = pd.read_excel(file_path, skiprows=28, nrows=22, usecols="A:D", sheet_name="Pier Load Summary")
df_2D = df.iloc[:,:2]
df_4D = df
assert len(df_2D.columns) ==2


def test_2D_input_case():
    output = format_data_for_training(df_2D)
    assert len(output.columns) == 1
    assert isinstance(output, pd.DataFrame)

def test_3D_and_up_input_case():
    output = format_data_for_training(df_4D)
    assert len(output.columns) == 3
    assert isinstance(output, pd.DataFrame)

