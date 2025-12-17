# namedtuple 사용하기
from collections import namedtuple
import operator

PEOPLE = [("Donald", "Trump", 7.85),
			("Vladimir", "Putin", 3.626),
			("Jinping", "Xi", 10.603)]

def format_sort_records(people_list):
    output = []
    info = namedtuple("Person", "lastname firstname time")
    preson1 = Person("asdf asdf asdf")
    template = "{1:10} {0:10} {2:5.2f}"
    for person in sorted(people_list, key = operator.itemgetter(1,0)):
        output.append(template.format(*person))
    return "\n".join(output)

print(format_sort_records(PEOPLE))