import threading

def my_thread():
    globals()['my_global_variable'] = 10

thread = threading.Thread(target=my_thread)
thread.start()

# Wait for the thread to finish
thread.join()

# Print the value of the global variable
print(globals()['my_global_variable'])