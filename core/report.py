class Report:
    ok: bool
    sys_message: str
    data: list[dict] | list[str]

    def __init__(self, ok: bool, sys_message: str, data: list[dict] | list[str] = list()):
        self.ok = ok
        self.sys_message = sys_message
        self.data = data