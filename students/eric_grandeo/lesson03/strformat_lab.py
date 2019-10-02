#!/usr/bin/env python3

#Task One

s = "file_{:0>3d} :  {:.2f}, {:.2e}, {:.2e}"

print(s.format( 2, 123.4567, 10000, 12345.67))

#Task Two
file = 2
num1 = 123.4567
num2 = 10000
num3 = 12345.67

print(f"file_{file:0>3d} :  {num1:.2f}, {num2:.2e}, {num3:.2e}")

#Task Three
#"the 3 numbers are: {:d}, {:d}, {:d}".format(1,2,3)

def formatter(in_tuple):
    l = len(in_tuple)
    form_string = "the {} numbers are: " + ",".join(["{}"]*l)
    return form_string.format(l,*in_tuple)


print(formatter((2,3,5)))
print(formatter((2,3,5,7,9)))


#Task Four
def task_four(tup):
    new_string = "{:0>2d}, {}, {}, {:0>2d}, {}"
    return new_string.format(tup[3], tup[4], tup[2], tup[0], tup[1])

print(task_four((4, 30, 2017, 2, 27)))
#'02 27 2017 04 30'




