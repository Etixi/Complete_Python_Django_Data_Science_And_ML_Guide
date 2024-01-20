try:
    salary = int(input("Enter salary amount: "))
    days_qty = int(input("Enter days quantity: "))
    salary_per_day = round(salary / days_qty)


except ValueError as e:
    print(e)
    print("Cannot convert value to integer")
except ZeroDivisionError as e:
    print(e)
    print("Cannot divide by zero!")
else:
    print("Result, salary per day: ", salary_per_day)
finally:
    print("Salary operation calculation complete")



# except Exception as e:
#     print("Some error happened")


# except Exception as e:
#     print(type(e))
#     print(e)
#     print(isinstance(e, Exception))
#     print(isinstance(e, ValueError))
#     print(isinstance(e, ZeroDivisionError))


# except (ValueError, ZeroDivisionError) as e:
#     if type(e) == ValueError:
#         print(e)
#         print("Cannot convert value to int")
#     if type(e) == ZeroDivisionError:
#         print(e)
#         print("Cannot divide by zero")


# except (ValueError, ZeroDivisionError) as e:
#      print(e)
#      print(type(e))
#      print("Some Error occurred")

