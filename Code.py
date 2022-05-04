"""
This program generates passages that are generated in mad-lib format
Author: Katherin 
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print("Lets create somehting")

name = raw_input("Please enter your name: ")

adj1 = raw_input("Enter an adjective (Ex: beautiful, smooth, nice): ")
adj2 = raw_input("Enter a secound adjective (Ex: Charming, Cruel, Fantastic): ")
adj3 = raw_input("and a third adjective (Ex: Gentle, great, perfect): ")


verb = raw_input("Enter a verb now (Ex: fighting, climbing, eating): ")

noun1 = raw_input("Now a noun (Ex: time, school, shoes): ")
noun2 = raw_input("Enter another noun (Ex: man, teacher, car): ")

animal = raw_input("Enter an animal ( Ex: rabbit, snail): ")
food = raw_input("Enter a food (Ex: Pasta, cake): ")
fruit= raw_input("Enter a fruit (Ex: Banana, grape): ")
superhero = raw_input("Enter a superhero (Ex: superman, Batman): ")
country = raw_input("Enter a country (Ex: Bangladesh, USA): ")
dessert = raw_input("Enter a dessert (Ex: Cake, donut): ")
year = raw_input("Enter a year (Ex: 2019,2020): ")

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)





















