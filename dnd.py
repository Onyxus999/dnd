import xml.etree.ElementTree as ET
import random

# Import the Race, Class, and Background data
tree = ET.parse('data.xml')
root = tree.getroot()

# Arrays for storing and randomizing values.
all_races = []
all_jobs = []
all_backgrounds = []

for child in root:
    if child.tag == 'race':
        all_races.append(child)

    elif child.tag == 'class':
        all_jobs.append(child)

    elif child.tag == 'background':
        all_backgrounds.append(child)

## Eventual implimentation
#race = all_races[random.randrange(0, len(all_races))]

# FIXME
race = all_races[0]

job = all_jobs[random.randrange(0, len(all_jobs))]
background = all_backgrounds[random.randrange(0, len(all_backgrounds))]

ability_scores = {'str' : random.randrange(3,19), 'dex' : random.randrange(3,19), 'con' : random.randrange(3,19), 'int' : random.randrange(3,19), 'wis' : random.randrange(3,19), 'cha' : random.randrange(3,19)}
racial_abilities = []
job_features = []
background_features = []
age = "0"
alignment = ""
size = ""
speed = "0"
abilities = []

# Race Parsing
for child in race:
	if child.tag == 'abs':
		for attribute in child:
			ability_scores[attribute.tag] += int(attribute.attrib['value'])

	elif child.tag == 'age':
		low = 0
		high = 0
		for number in child:
			if number.tag == 'high':
				high = int(number.attrib['value'])
			elif number.tag == 'low':
				low = int(number.attrib['value'])
			else:
				pass
		age = random.randrange(low, high+1)

	elif child.tag == 'alignment':
		for aspect in child:
			civil = ""
			moral = ""
			if aspect.tag == 'civil':
				civil = aspect.attrib['value']
			elif aspect.tag == 'moral':
				moral = aspect.attrib['value']
			else:
				pass
		if civil == "":
			civilities = ["Lawful", "Neutral", "Chaotic"]
			civil = civilities[random.randrange(0, len(civilities))]
		if moral == "":
			moralities = ["Good", "Neutral", "Evil"]
			moral = moralities[random.randrange(0, len(moralities))]
		if civil == "Neutral" and moral == "Neutral":
			civil = "True"
		alignment = civil + " " + moral

	elif child.tag == 'size':
        	size = child.attrib['value']

	elif child.tag == 'speed':
                speed = child.attrib['value']

	elif child.tag == 'ability':
                abilities.append(child.attrib['name'] + ": " + child.attrib['desc'])
                

print "Name: " + "\tAge: " + str(age)
print "Race: " + race.attrib['name'] + "\tClass: " + job.attrib['name']
print "Background: " + background.attrib['name'] + "\tAlignment: " + alignment
print "Size: " + size + "\tSpeed: " + str(speed)
print "\nAbility Scores:\n\tSTR: " + str(ability_scores['str']) + "\n\tDEX: " + str(ability_scores['dex']) + "\n\tCON: " + str(ability_scores['con']) + "\n\tINT: " + str(ability_scores['int']) + "\n\tWIS: " + str(ability_scores['wis']) + "\n\tCHA: " + str(ability_scores['cha'])
print "--------- --------- ---------"
print "Abilities:"
for ability in abilities:
    print "\n\t" +  ability
