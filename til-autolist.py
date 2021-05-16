# This little script automatically creates README for this project
# and links all TILs appropriately... Gosh... The blessing of loops
from os import listdir, path

output = 'Things I Learned Today about programming languages, frameworks and libararies or technology in general  \n\n'
total = 0
for mainFile in listdir('.'):
	directory = filepath = ''
	if path.isdir(mainFile):
		output += '\n**' + mainFile.capitalize() + '**  \n'
		directory += mainFile
		current = 0
		for file in listdir(mainFile):
			if file.endswith('.md'):
				filepath = directory + '/' + file
				filetitle = file.replace('-', ' ').replace('.md', '').capitalize()
				output += f'- [{filetitle}]({filepath})  \n'
				current += 1
				total += 1

		print(f'{mainFile} = {current} files')

print(f'\n{total} total TILs so far\n')
file = open('README.md', 'w')
file.write(output)
file.close()