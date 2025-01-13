# `Recursion` is a concept where a function calls itself to solve smaller
# instances of the same problem

# The key components of recursion are:
# - Base Case: A condition that stops the recursion. Without a base case, a
#   function would keep calling itself indefinitely

# - Recursive Case: The part where the function calls itself with modified
#   parameters to gradually reach the base case

# Simplest Form:


def foo(n: int) -> int:
    # Base Case
    if n == 1:
        return 1

    # Recursive Case
    return n + foo(n - 1)


print(foo(10))


# The recursive function foo(n) computes the sum of all integers from 1 to n.
# It works by first checking the base case, where if n == 1, it returns 1. For
# larger values of n, it calls itself recursively with n - 1 and adds n to the
# result. This process continues until the base case is reached. As the recursive
# calls begin to unwind, each function call adds its value to the result from the
# previous call, summing all the integers from 1 to n. For example, foo(10)
# returns the sum of the numbers from 1 to 10, which is 55.

# foo(10)                 ---> 10 + foo(9)
#                         ---> 10 + (9 + foo(8))
#                         ---> 10 + (9 + (8 + foo(7)))
#                         ---> 10 + (9 + (8 + (7 + foo(6))))
#                         ---> 10 + (9 + (8 + (7 + (6 + foo(5)))))
#                         ---> 10 + (9 + (8 + (7 + (6 + (5 + foo(4)))))))
#                         ---> 10 + (9 + (8 + (7 + (6 + (5 + (4 + foo(3))))))))
#                         ---> 10 + (9 + (8 + (7 + (6 + (5 + (4 + (3 + foo(2))))))))))
#                         ---> 10 + (9 + (8 + (7 + (6 + (5 + (4 + (3 + (2 + foo(1)))))))))))
#
# foo(1)               ---> Returns 1 (Base case)
#
# Now, the recursion starts to unwind:
#
#                         ---> foo(1) = 1
#                                | (returns to foo(2))
#                                V
#                         ---> foo(2) = 2 + 1 = 3
#                                | (returns to foo(3))
#                                V
#                         ---> foo(3) = 3 + 3 = 6
#                                | (returns to foo(4))
#                                V
#                         ---> foo(4) = 4 + 6 = 10
#                                | (returns to foo(5))
#                                V
#                         ---> foo(5) = 5 + 10 = 15
#                                | (returns to foo(6))
#                                V
#                         ---> foo(6) = 6 + 15 = 21
#                                | (returns to foo(7))
#                                V
#                         ---> foo(7) = 7 + 21 = 28
#                                | (returns to foo(8))
#                                V
#                         ---> foo(8) = 8 + 28 = 36
#                                | (returns to foo(9))
#                                V
#                         ---> foo(9) = 9 + 36 = 45
#                                | (returns to foo(10))
#                                V
#                         ---> foo(10) = 10 + 45 = 55
#                                | (returns to function caller)
#                                V
#
# Final result: foo(10) = 55

# The function traverses down the stack until it reaches the base case, then
# unwinds up the stack, eventually returning to the function caller

# This process can be broken down into three steps:
# - Pre: The expression before the recursive call (e.g., n + [Recursive Call])
# - Recurse: The function calls itself recursively
# - Post: Actions performed after the recursion finishes

# Each time a function is called, it uses a `return address` to determine where
# to send the `return value` once the function finishes executing. Additionally,
# any `arguments` passed to the function are stored in its `stack frame`. All of
# these values—return address, return value, and function arguments—require
# memory space, which is allocated in the `stack` for the duration of the function call
