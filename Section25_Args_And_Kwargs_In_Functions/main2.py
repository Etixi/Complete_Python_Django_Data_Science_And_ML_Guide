print()
print("Practice - Working with Keyword Arguments" + "\n" +
      "=============================================")
print()

def comments_info(comments_qty, day):
    print(f'{comments_qty} comments were posted on {day}')

def comments_info_args(*args):
    print(f'{args[0]} comments were posted on {args[1]}')

comments_info_args(50, 'Monday')
comments_info(comments_qty=50, day='Monday')
comments_info(50, day='Monday')