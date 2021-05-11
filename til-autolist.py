# This little script automatically creates README for this project
# and links all TILs appropriately... Gosh... The blessing of loops
from os import listdir, path

output = 'Things I Learned Today about programming languages, frameworks and libararies or technology in general  \n\n'
for mainFile in listdir('.'):
	directory = filepath = ''
	if path.isdir(mainFile):
		output += '\n**' + mainFile + '**  \n'
		directory += mainFile
		for file in listdir(mainFile):
			if file.endswith('.md'):
				filepath = directory + '/' + file
				output += f'- [{file}]({filepath})  \n'

file = open('README.md', 'w')
file.write(output)
file.close()