import multiprocessing

# Function must be in the global namespace
def worker(x):
    return x * x

if __name__ == '__main__':
    # One worker processes per processor
    pool = multiprocessing.Pool()
    # Distributes the sequence xrange(10) in batches to the worker processes,
    # which pull work items off a queue.
    # The worker processes run worker(...)
    # For example, if there are two processors,
    # processor 1 will get 0, processor 2 will get 1
    # When processor 1 has finished with 0 it will get 3, and so on.
    results = pool.map(worker, xrange(10))
    print results
