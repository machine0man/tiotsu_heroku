from mapbox import Datasets

access_token="sk.eyJ1Ijoic2hhbmtvaWJpdG8iLCJhIjoiY2pidGk1NHVyMWhsNDJxcm5qMzk1NjdjbSJ9.eVgFTGreLyiND18CkqNS8w"

datasets = Datasets()
datasets.list_features("cjbphbl3008s833ntx1t5psea").json()
