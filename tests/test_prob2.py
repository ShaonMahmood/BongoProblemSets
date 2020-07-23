import pytest
from bongo2 import calculate_depth, print_depth, dictionary_input


@pytest.mark.parametrize("unwanted_input", ["", 3])
def test_raises_exception_on_non_dict_arguments(unwanted_input):
    with pytest.raises(TypeError):
        calculate_depth(unwanted_input)


@pytest.mark.parametrize("input_dict, expected_result", [
    (
        {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                }
            }
        },
        [("key1", 1), ("key2", 1), ("key3", 2), ("key4", 2), ("key5", 3)]
    ),
    (
        dictionary_input(),
        [("key1", 1), ("key2", 1), ("key3", 2), ("key4", 2), ("key5", 3), ("user", 3),
         ("first_name", 4), ("last_name", 4), ("father", 4),
         ("first_name", 5), ("last_name", 5), ("father", 5),
        ]
    ),
    (
        {},
        []
    ),
])
def test_calculate_depth_of_dict_with_object(input_dict, expected_result):
    assert calculate_depth(input_dict) == expected_result
