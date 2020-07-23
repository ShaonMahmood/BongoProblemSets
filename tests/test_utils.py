import pytest
from utils import object_to_dict, first_common_occurrence
from bongo2 import Person


@pytest.mark.parametrize("unwanted_builtin_input", ["", 3, []])
def test_raises_exception_on_builtin_arguments(unwanted_builtin_input):
    with pytest.raises(TypeError):
        object_to_dict(unwanted_builtin_input)


@pytest.mark.parametrize("input_object, expected_result", [
    (
        Person("User", "1", None),
        None
    ),
    (
        Person("User", "2", "father"),
        "father"
    ),
])
def test_object_to_dict_function(input_object, expected_result):
    actual_result = object_to_dict(input_object)["father"]
    assert actual_result == expected_result


@pytest.mark.parametrize("unwanted_input", [[2,[1,3]],[[1,3],3]])
def test_raises_exception_on_non_sequence_arguments(unwanted_input):
    with pytest.raises(TypeError):
        first_common_occurrence(unwanted_input[0], unwanted_input[1])


@pytest.mark.parametrize("input_sequences, expected_result", [
    (
        [[2,3,4,6,1], [5,2,1]],
        2
    ),
    (
        [[4,3,2,1],[9,7,5,4,1]],
        4
    ),
])
def test_first_common_occurrence(input_sequences, expected_result):
    actual_result = first_common_occurrence(input_sequences[0], input_sequences[1])
    assert actual_result == expected_result