import pytest
import sys
from pathlib import Path

# Add the parent directory to sys.path
parent_dir = Path(__file__).parent.parent.resolve()
sys.path.append(str(parent_dir))

from excel_input_parser import ExcelInputParser

@pytest.fixture
def excel_input_parser():
    return ExcelInputParser()


def test_parse_input_w_sheet_name_single_range(excel_input_parser):
    excel_input_parser.parse_input("Sheet123!A2:B9")
    assert excel_input_parser.sheet_name =="Sheet123"
    assert excel_input_parser.cell_range == "A2:B9"
    usecols = excel_input_parser.extract_usecols()
    assert usecols == "A:B"
    skiprows, nrows = excel_input_parser.extract_rows()
    assert skiprows == 1
    assert type(skiprows) == int
    assert nrows == 8
    assert type(nrows) == int


def test_parse_input_wo_sheet_name_single_range(excel_input_parser):
    excel_input_parser.parse_input("A2:B9")
    assert excel_input_parser.sheet_name == 0
    assert excel_input_parser.cell_range == "A2:B9"

def test_parse_input_w_sheet_name_multi_range(excel_input_parser):
    excel_input_parser.parse_input("Sheet123!A2:B9,F,G")
    assert excel_input_parser.sheet_name =="Sheet123"
    assert excel_input_parser.cell_range == "A2:B9,F,G"
    usecols = excel_input_parser.extract_usecols()
    assert usecols == "A:B,F,G"
    skiprows, nrows = excel_input_parser.extract_rows()
    assert skiprows == 1
    assert type(skiprows) == int
    assert nrows == 8
    assert type(nrows) == int




