import logging


class LogParser:
    def parse(self, filename: str) -> list[str]:
        logLines = self.loadLines(filename)
        hexes = self.parseHexes(logLines)
        unifyLines = self.unifyLines(hexes)
        sids = self.parseSids(unifyLines)
        return sids

    def loadLines(self, filename: str) -> list[str]:
        lines: list[str] = []
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
        except FileNotFoundError:
            logging.error('Файл логов не найден')
            raise
        return lines

    def parseHexes(self, lines: list[str]):
        parsed: list[str] = []
        for line in lines:
            index_of_ampersand = line.find('&')
            parsed.append(
                line[index_of_ampersand + 8:index_of_ampersand + 12]
            )

        return parsed

    def unifyLines(self, lines: list[str]) -> list[str]:
        return set(lines)

    def hexToDecimal(self, hex_str: str) -> (str | None):
        try:
            return str(int(hex_str, 16))
        except ValueError:
            return None

    def parseSids(self, lines: list[str]):
        decimals: list[str] = []
        for line in lines:
            decimal = self.hexToDecimal(line)
            if decimal is not None:
                decimals.append(decimal)
        return decimals
