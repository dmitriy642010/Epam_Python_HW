import pytest
from code_bags import make_filter

sample_data = [
    {
        "name": "Bill",
        "last_name": "Gilbert",
        "occupation": "was here",
        "type": "person",
    },
    {"is_dead": True, "kind": "parrot", "type": "bird", "name": "polly"},
    {"is_dead": True, "kind": "crow", "type": "bird", "name": "hunter"},
]


@pytest.mark.parametrize(
    ("value", "expected_result"),
    [
        ({"name": "polly", "type": "bird"}, [sample_data[1]]),
        ({"type": "bird"}, [sample_data[1], sample_data[2]]),
    ],
)
def test_make_filter(value, expected_result):
    assert make_filter(**value).apply(sample_data) == expected_result
