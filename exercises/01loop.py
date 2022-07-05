# Write a function called `p_times` that takes a `statement` and
# a `num` as inputs, and outputs the `statement` some `num` of times
# to the console.
#
# Example function call:
#
# p_times('Hello there', 1)
#
# > Hello there
#
# p_times('Hello there', 3)
#
# > Hello there
# > Hello there
# > Hello there

# p_times = ["u suck"]*17

# print(p_times)

def p_times(statement, num):
    for p in range(1, num+1):
        print(statement)
p_times("u suck", 3)