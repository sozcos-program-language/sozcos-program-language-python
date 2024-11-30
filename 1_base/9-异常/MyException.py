try:
    print(1/1)
except Exception as e:
    print('An error occurred:', e)
else:
    print('No error occurred.')
finally:
    print('This code will always run.')