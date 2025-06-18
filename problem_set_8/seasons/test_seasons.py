from seasons import validate
import pytest

def test_exit():
    with pytest.raises(SystemExit) as e:
        validate("January 25, 1996")
    assert e.type == SystemExit

    with pytest.raises(SystemExit) as e:
        validate("")
    assert e.type == SystemExit

   