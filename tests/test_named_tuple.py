import pytest
import rapidjson
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])


@pytest.mark.unit
def test_named_tuple():
    p = Point(x=1, y=2)
    dumped = rapidjson.dumps(p)
    loaded = rapidjson.loads(dumped)
    expected = p._asdict()
    assert loaded == expected
