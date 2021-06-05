
from src.google_sheet import read_google_sheet


def test_download_data_from_cloud():

    data = read_google_sheet()
    assert isinstance(data, dict)
