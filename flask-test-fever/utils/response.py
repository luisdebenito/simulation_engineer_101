class Response:
    @staticmethod
    def ok_query(data):
        return (
            data,
            200,
            {"Content-Type": "application/json"},
        )

    @staticmethod
    def error(msg:str, code:int):
        return ({"err": msg}, code, {"Content-Type": "application/json"})

    @staticmethod
    def ok_mut():
        return (
            "",
            200,
            {"Content-Type": "application/json"},
        )