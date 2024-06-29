import time


def timeit(x1):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(start_time)
        result = x1(*args, **kwargs)
        end_time = time.time()
        actual_time_taken = start_time - end_time
        print(f"the time taken by the decorator to run is {actual_time_taken:.6f}")
        return result

    return wrapper


# keyword arguments: name="energy".
# positional arguments: 2, 4, 6.


@timeit
def add_numbers(x, y, z, name="energy", age=9999999):
    list_1 = [x, y, z, name, age]
    return list_1


sum_result = add_numbers(3, 6, 5, name="energy", age=9999999)
print(sum_result)
