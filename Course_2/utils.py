import time


def timeit(action_str="Starting", print_time=True):
    """ decorator to time and print exec time and text """

    def inner_function(func):
        def wrapper(*arg, **kwarg):
            start_time = time.time()
            print(action_str.center(100, "="))
            res = func(*arg, **kwarg)
            t = int(time.time() - start_time)
            if t > 5:  # in min and seconds
                m, s = t // 60, t % 60
                time_str = "{:0>2.0f}:{:0>2.0f}s".format(m, s)
            else:  # in milliseconds
                time_str = "{:.0f}ms".format(t * 1000)
            s = " {}: Done ".format(action_str)
            s += print_time * "in  {}".format(time_str)
            print(s.center(100, "="))
            return res

        return wrapper

    return inner_function
