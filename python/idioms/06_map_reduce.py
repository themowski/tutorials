# Before list comprehensions you used some common sequence->sequence functions
# from functional programming, such as map and reduce.

# map(function, iterable, ...)
# Apply function to every item of iterable and return a list of the results.
number_texts = map(lambda i: "Number %u" % i, xrange(100))
print number_texts

# reduce(function, iterable[, initializer])
# Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
joined_number_texts = reduce(lambda left, right: left + ' ' + right, number_texts)
print joined_number_texts

# map and reduce can be parallelized easily to work on very large sequences by partitioning
# the input sequence among many nodes:
# This is the basic approach of Hadoop, an implementation of Google's MapReduce system.
# Hadoop is one of the main tools used in "Big Data".
# From https://en.wikipedia.org/wiki/MapReduce
#   "Map" step: Each worker node applies the "map()" function to the local data, and writes the output to a temporary storage. A master node orchestrates that for redundant copies of input data, only one is processed.
#   "Shuffle" step: Worker nodes redistribute data based on the output keys (produced by the "map()" function), such that all data belonging to one key is located on the same worker node.
#   "Reduce" step: Worker nodes now process each group of output data, per key, in parallel.
# One of the classic use cases is
# map(log lines) -> {log element 1: count, log element 2: count}
# shuffle -> send all log element 1: counts to the same node
# reduce: sum all of the log element 1: counts