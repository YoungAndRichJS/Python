# zip 함수 구현
def myzip(*iterables):
    output = []
    min_len = min(len(it) for it in iterables)
    for i in range(min_len):
        yield tuple(it[i] for it in iterables)

print(list(myzip([10,20,30], "abc") ))
print(list(myzip([10,20,30], "abc", [100,200,300])))