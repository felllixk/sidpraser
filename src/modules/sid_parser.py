import logging
from typing import Any, Optional, TypeGuard
import bs4
import requests


class SidParser:
    url: str = ''
    sids: dict[str] = {}

    def __init__(self, url):
        self.url = url

    def parse(self) -> dict[str]:
        bs = self._prepareBeautifulSoup(self.url)
        sidTables = self._getSidTables(bs)
        sidRows = self._getTableRows(sidTables)
        return self._getSids(sidRows)

    def _isTag(self, element: Any) -> TypeGuard[bs4.element.Tag]:
        return isinstance(element, bs4.element.Tag)

    def _prepareBeautifulSoup(self, url: str) -> bs4.BeautifulSoup:
        try:
            response = requests.get(url)
            response.raise_for_status()
            return bs4.BeautifulSoup(response.text, "html.parser")

        except requests.RequestException as e:
            logging.error(f"Ошибка сетевого запроса: {e}")
            raise

    def _getSidTables(self, bs: bs4.BeautifulSoup) -> bs4.ResultSet[Any]:
        return bs.findAll('table', {"width": "720", 'border': ''})

    def _getTableRows(self, sidTables: bs4.ResultSet[Any]) -> list[bs4.element.Tag]:
        result = []
        for table in sidTables:
            if not self._isTag(table):
                logging.warning('Element is not type of bs4.element.Tag')
                continue
            rows = table.findChildren('tr')

            for row in rows[2:]:
                if self._isTag(row):
                    result.append(row)
        return result

    def _getTagValue(self, tag: Any):
        return tag.getText(strip=True).replace(' ', '') if self._isTag(tag) else None

    def _getSids(self, tableRows: list[bs4.element.Tag]):
        sids = {}
        for row in tableRows:
            rowValues = row.findChildren('td')

            if len(rowValues) in [9, 11]:
                sid_index = 0 if len(rowValues) == 9 else 2
                channel_index = 3 if len(rowValues) == 9 else 5
                sid = self._getTagValue(rowValues[sid_index])
                channel = self._getTagValue(rowValues[channel_index])
                sids[sid] = channel

        return sids
