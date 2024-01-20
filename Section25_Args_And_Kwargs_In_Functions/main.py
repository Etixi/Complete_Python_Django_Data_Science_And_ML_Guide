print()
print("Practice - Using *args to Gather Positional Arguments into a Tuple" + "\n" +
      "===================================================================")
print()

def sort_nums(*args):
    return sorted(args, reverse=True)
    # for arg in sorted(args, reverse=True):
    #    print(arg)

sorted_nums = sort_nums(10, 3, 15, 246, 23)
print(sorted_nums)

sorted_nums = sort_nums(377, 23, 3)
print(sorted_nums)


