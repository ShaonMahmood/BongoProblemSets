from collections import deque
from utils import measureTime, object_to_dict


class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father


def dictionary_input():
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


def calculate_depth(d):
    """

    :param d: the dictionary for which depth will be measured
    :return: returns a list of tuples with depth result for each key
    """
    if not isinstance(d, dict):
        raise TypeError('Please provide a dict argument')

    final_result = list()
    queue = deque([(id(d), d, 1)])
    memo = set()
    while queue:
        id_, o, level = queue.popleft()
        if id_ in memo:
            continue
        memo.add(id_)

        if isinstance(o, Person):
            o = object_to_dict(o)

        if isinstance(o, dict):
            for key in o.keys():
                # print(f"{key} {level}")
                final_result.append((key,level))
            queue += ((id(v), v, level + 1) for v in o.values())
    return final_result


@measureTime
def print_depth(input_dict):
    result_list = calculate_depth(input_dict)
    for key, level in result_list:
        print(f"{key} {level}")


if __name__ == "__main__":
    print_depth(dictionary_input())
