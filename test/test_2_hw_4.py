from unittest.mock import MagicMock, patch
from urllib.error import HTTPError

from Epam_training_HW.hw.hw_4_task_2 import count_dots_on_i

import pytest


@patch("urllib.request.urlopen")
def test_count_dots_on_i(mock_urlopen):
    m_mock = MagicMock()
    m_mock.read.return_value = b"iii"
    mock_urlopen.return_value = m_mock
    res = count_dots_on_i(m_mock)
    assert res == 3


@patch("urllib.request.urlopen")
def test_unreachable_url(mock_urlopen):
    m_mock = MagicMock()
    mock_urlopen.side_effect = HTTPError(
        "http://example.com", 500, "Internal Error", {}, None
    )
    with pytest.raises(ValueError, match="Unreachable {url}"):
        count_dots_on_i(m_mock)
