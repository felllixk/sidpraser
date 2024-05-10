import logging


class LogParser:
    def parse(self, filename: str) -> list[str]:
        rawParsedLines = self.loadLines(filename)
        unifyLines = self.unifyLines(rawParsedLines)
        sids = self.parseSids(unifyLines)
        return sids

    def loadLines(self, filename: str) -> list[str]:
        parsedLines: list[str] = []
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    index = line.find('0B00&000000/')
                    if index != -1:
                        shortened_line = line[index +
                                              len('0B00&000000/'):index + len('0B00&000000/') + 4]
                        parsedLines.append(shortened_line)
                    else:
                        parsedLines.append(line)
        except FileNotFoundError:
            logging.error('Файл логов не найден')
            raise
        return parsedLines

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
