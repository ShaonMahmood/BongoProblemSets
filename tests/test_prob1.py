import pytest
from bongo1 import calculate_depth


@pytest.mark.parametrize("unwanted_input", ["", 3])
def test_raises_exception_on_non_dict_arguments(unwanted_input):
    with pytest.raises(TypeError):
        calculate_depth(unwanted_input)


@pytest.mark.parametrize("input_dict, expected_result", [
    ({
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
            }
        }
    }, [("key1", 1), ("key2", 1), ("key3", 2), ("key4", 2), ("key5", 3)]),
    ({}, []),
])
def test_calculate_depth_of_dict(input_dict, expected_result):
    assert calculate_depth(input_dict) == expected_result
