from PyQt6.QtWidgets import QTableWidget, QTableWidgetItem


class TableManager:
    def __init__(self, table: QTableWidget):
        self.table = table

    def add_row(self, data):
        row_count = self.table.rowCount()
        self.table.insertRow(row_count)
        for column, value in enumerate(data):
            item = QTableWidgetItem(str(value))
            self.table.setItem(row_count, column, item)

    def remove_row(self, row_index):
        self.table.removeRow(row_index)

    def clear_table(self):
        self.table.setRowCount(0)

    def set_data(self, data):
        self.clear_table()
        for row_data in data:
            self.add_row(row_data)
