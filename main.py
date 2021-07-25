# This prints a fibonnaci sequence for as long as n


def fib(n):
    a = 0;
    b = 1;
    for number in range(n):
        a, b = b, a + b;

        print(a)


    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


fib(10)