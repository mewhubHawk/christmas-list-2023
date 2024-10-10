import time
import datetime

delay=1.0  
 
def FormatedList(title, presents_file, delay):
  with open(presents_file) as file:
    presents_list = file.readlines()
    
  print(title)
  time.sleep(0.4)
  for item in presents_list:
    print(f'--{item.strip()}') 
    time.sleep(delay)
  print(" ")

print("My Christmas List \n")

now = time.time()
time.sleep(0.4)
christmas = time.strptime("25 dec 23", "%d %b %y")
how_long_to_wait = time.mktime(christmas) - now

print(f'Today is {time.asctime()}.')
time.sleep(0.4)

print(f'christmas is {time.asctime(christmas)}')
time.sleep(0.5)

print("That's {} to go... \n".format(datetime.timedelta(seconds=how_long_to_wait)))
time.sleep(0.6)

FormatedList("1. BOOKS(novels):", "books.txt", delay)
FormatedList("2. MANGA:", "mangas.txt", delay)
FormatedList("3. TO MAKE JELLYFISH LIGHTS:", "jellyfish.txt", delay)
