#this funtions takes an input num1 and num2 and reverses it through the nagative slicing
#recall...
#stuff = "something"
#stuff[:] gives back all the value of stuff
#stuff[2::]gives back value from index 2 to the end
#stuff[0::2]gives back value from index 0 to the end but with a step of 2. i.e it skips one
#remember you can use nagative indexing to retrieve values from the last we use the same concept to slice in the reverse order
#so stuff[6:1:-1] returns from  1 backwards to 0

def reverse_sum(num1, num2):
    return int(str(num1)[::-1][::-1]) + int(str(num2)[::-1][::-1])

print(reverse_sum(13, 14))

#note that you can't perform the same indexing or slicing on a integer
#what you need to do is to frist convert the int to str
#for example a way to reserve an integer;
#num = 12345
#***convert the num to a string***
#str_num = str(num)
#***reverse the string***
#str_num_reversed = str_num[len(str_num)::-1]-------should return 54321
#int(str_num_reversed)----should return 54321
