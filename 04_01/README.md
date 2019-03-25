# Using Try/Except Blocks for Error Handling

```Python
try:
    # f = open('test_file.txt')
    f = open('corrupt_file.txt')
    # if f.name == 'corrupt_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Excuting Finally...")
```