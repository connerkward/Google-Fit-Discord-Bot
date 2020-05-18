import threading
import time
import webhook_discord


def countdown(count):
    while count > 0:
        count -= 1


count = 50000000
# Threading example

start = time.time()
countdown(count)
end = time.time()
print(f"On one thread, countdown takes {end - start} seconds")

# Creates threads that when started execute COUNTDOWN with argument COUNT//2
t1 = threading.Thread(target=countdown, args=(count//2,))
t2 = threading.Thread(target=countdown, args=(count//2,))

start = time.time()
# The thread functions execute with their arguments
t1.start()
t2.start()
# join() ensures that these threads complete before the main program continues execution
t1.join()
t2.join()
end = time.time()
print(f"On two threads, countdown takes {end - start} seconds")

webhook_url = "https://discordapp.com/api/webhooks/708841556571848725/zJoGnm5jKbS6y6WRf5xCUKB4fIo7v0L2VBzemRa6pGkoeBYwzLgd9IhQ75cUeqGkLC6q"
content1 = {'content':'Test 1'}
content2 = {'content': 'Test2'}

t3 = threading.Thread(target=webhook_discord.send, args=(content1, webhook_url,))
t4 = threading.Thread(target=webhook_discord.send, args=(content2, webhook_url,))

t3.start()
t4.start()

# Because of the GIL, Python does not run these in parallel, but periodically switches between threads
