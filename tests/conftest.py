import pytest
from bongo2 import Person


@pytest.fixture
def example_dictionary_data():
    return {
        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 4,
            }
        }
    }


@pytest.fixture
def example_dictionary_data_with_objects():
    person_a = Person("User", "1", None)
    person_b = Person("User", "2", person_a)
    d = {

        "key1": 1,
        "key2": {
            "key3": 1,
            "key4": {
                "key5": 1,
                "user": person_b
            }
        }
    }
    return d


