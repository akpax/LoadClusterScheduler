import re

class ExcelInputParser:
    def __init__(self):
        self.sheet_name = None
        self.cell_range = None

    def parse_input(self, user_input):
        """
        Parses the user input into the sheet name and cell range.
        If there is no sheet name, then it returns zero for the sheet name.
        """
        if "!" in user_input:
            self.sheet_name, self.cell_range = user_input.split("!")
        else:
            self.sheet_name = 0  # assume only 1 sheet with index 0
            self.cell_range = user_input

    def extract_usecols(self):
        """
        Extracts column labels from the cell range.
        """
        return "".join([char for char in self.cell_range if not char.isdigit()])

    def extract_rows(self):
        """
        Extracts row indices from the cell range and returns skiprows and nrows.
        """
        numbers = re.findall(r"\d+", self.cell_range)
        numbers = list(map(int, numbers))
        start_row = min(numbers)
        end_row = max(numbers)
        skiprows = start_row -1
        nrows = end_row - start_row + 1
        return skiprows, nrows
