def func():
    print('This is a message from the function in the imported module.')

if __name__ != "__main__":
    print(f'This is a message from {__name__}.')

# Make a change here.
else:
    print('This should not be printed')

