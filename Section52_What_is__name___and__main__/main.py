"""
print("========== Practice - __name__ ==================")

print(dir())
print(__name__)
print(type(__name__))
print('MAIN', __name__)
print('MAIN', __name__ == '__main__')

if __name__ == '__main__':
    print('MAIN : ', 'ONLY IF RUN DIRECTLY')

"""

print("========== Example - Executing Functions only when Module is run Directly ==================")
def initialize():
    # Code to initialize application and perform
    print("Initializing ....")

def main():
    # Code for main app functionality
    print("Running main functionality")

if __name__ == '__main__':
    initialize()
    main()

