import time


def timeit(action_str="Starting", print_time=True):
    """ decorator to time and print exec time and text """

    def inner_function(func):
        def wrapper(*arg, **kwarg):
            start_time = time.time()
            print(action_str.center(100, "="))
            res = func(*arg, **kwarg)
            t = int(time.time() - start_time)
            m, s = t // 60, t % 60
            print(
                (
                    " {}: Done ".format(action_str)
                    + print_time * "in {:0>2.0f}:{:0>2.0f}s ".format(m, s)
                ).center(100, "=")
            )
            return res

        return wrapper

    return inner_function
