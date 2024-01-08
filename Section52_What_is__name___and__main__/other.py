"""
print("========== Practice - __main__ ==================")

print('OTHER', __name__)
print('OTHER', __name__ == '__main__')

if __name__ == '__main__':
    print('OTHER : ', 'ONLY IF RUN DIRECTLY')
"""

print("========== Example - Executing Functions only when Module is run Directly ==================")
from main import initialize, main
initialize()
main()