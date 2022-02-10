from googleapiclient.discovery import build


class MiniSearchEngineAction:
    def __init__(self) -> None:
        pass

    def Search(self, q, startIndex=1):
        service = build("customsearch",
                        "v1",
                        developerKey="AIzaSyCiCMOBoz7K6e40pQZyLwMm2bDE2JozRgU")
        res = service.cse().list(
            q=q,
            start=startIndex,
            cx="847ba8eb41420b215",
        ).execute()
        res = dict(res)
        return res
