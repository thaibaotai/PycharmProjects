import some_module

print(f'This is a message from {__name__}.')
some_module.func()# Call func() from the imported module

# Make a change here.
if __name__ == "__main":
    print('This should be printed ONLY when task.py is called directly.')

