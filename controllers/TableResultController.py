from PyQt6.QtWidgets import QHeaderView, QSizePolicy, QTableWidget
from app.container import Container


class TableResultController:
    def __init__(self, container: Container):
        self.window = container.getWindow()
        self.setup_style()

    def setup_style(self):
        # Получаем таблицу из интерфейса
        table = self.window.nodes.getTableResult()

        # Настройка таблицы для возможности только копирования
        self.setup_copy_only(table)

        # Устанавливаем режим растяжения колонок
        header = table.horizontalHeader()

        # Первая колонка изменяемая пользователем
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Interactive)
        # Устанавливаем начальную и максимальную ширину первой колонки
        initialWidth = table.width()
        initialColumnWidth = int(initialWidth * 0.3)
        table.setColumnWidth(0, initialColumnWidth)
        table.horizontalHeader().setMaximumSectionSize(int(initialWidth * 0.5)
                                                       )  # Например, максимум 50% от ширины таблицы

        # Вторая колонка растягивается на все оставшееся пространство
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)

        # Для обеспечения пересчета размеров при изменении размера окна
        table.setSizePolicy(QSizePolicy.Policy.Expanding,
                            QSizePolicy.Policy.Expanding)
        table.resizeEvent = self._handleResize

    def setup_copy_only(self, table: QTableWidget):
        # Выключаем возможность редактирования
        table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        # Включаем возможность выделения текста
        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectItems)

    def _handleResize(self, event):
        # Пересчитываем размер первой колонки при изменении размера таблицы
        table = self.window.nodes.getTableResult()
        initialWidth = table.width()
        # Обновляем максимальную ширину первой колонки
        table.horizontalHeader().setMaximumSectionSize(int(initialWidth * 0.5))
        super(type(table), table).resizeEvent(event)
