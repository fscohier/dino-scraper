# Required libraries
import requests
from bs4 import BeautifulSoup
import csv

# wikipedia url where dinosaur names are
url = "https://en.wikipedia.org/wiki/List_of_dinosaur_genera"

# 1 - Let's fetch the webpage content
response = requests.get(url)
if response.status_code == 200:
    print("Page successfully fetched!")
else:
    print(f"Page failed to be fetched. Status code: {response.status_code}")

# 2 - Let's parse the HTML through BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

# 3 - Let's extract the dino names
# After analysis of the html page, the dino names are listed as li elements and with italics
dinosaur_list = []

# Let's find all ul elements
for ul in soup.find_all("ul"):
    # Let's iterate through each li element
    for li in ul.find_all("li"):
        # Let's find the italics and append if not already in the list
        dinosaur_name = li.find("i").text if li.find("i") else None
        if dinosaur_name and dinosaur_name not in dinosaur_list:
            dinosaur_list.append(dinosaur_name)

# 4 - Let's clean up the list of items longer than 1 word
clean_dinosaur_names = [
    name for name in dinosaur_list
    if len(name.split()) == 1
]

# 5 - Let's sort it by alphabetical order
sorted_dinosaur_list = sorted(clean_dinosaur_names)

# 6 - Let's save the file to CSV
csv_file = "dinosaur_list.csv"

with open(csv_file, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Dino Name"])
    for name in sorted_dinosaur_list:
        writer.writerow([name])

# 7 - Let's just confirm everything was done successfully and print the 666th dino name.
print(f"{len(sorted_dinosaur_list)} dinosaurs were found!")
print(f"The names are saved to '{csv_file}'")
print(f"An evil dinosaur name is {sorted_dinosaur_list[666]}.")
