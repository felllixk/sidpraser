
class SidAssociator:
    logSids: list[str] = []
    result: list[str | None] = []

    def associateSid(self, sidMap: dict[str], logSids: list[str]) -> dict[str | None]:
        map: dict[str | None] = {}
        for sid in logSids:
            map[sid] = sidMap.get(sid, None)
        return map

    def storeResult(self, filepath: str, map: dict[str | None]) -> None:
        with open(filepath, 'w+', encoding='utf-8') as f:
            for sid, channel in map.items():
                f.write(f"{sid} {channel if channel is not None else ''}\n")
