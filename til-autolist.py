from os import listdir, path

output = 'Small markdown files documenting small things I learn every day. These can be anything from a small command to a small code snippet. The goal is to have a collection of small things that I can refer to later.\n\n'

total = 0
directories = {}

# Collect directories and count markdown files
for mainFile in listdir('.'):
	if path.isdir(mainFile):
		quickTotal = sum(1 for file in listdir(mainFile) if file.endswith('.md'))
		directories[mainFile] = quickTotal

# Sort directories alphabetically
sorted_directories = sorted(directories.keys())

for mainFile in sorted_directories:
	if directories[mainFile] > 0:  # Only include categories with at least one markdown file
		output += f'\n**{mainFile.capitalize()}**  \n'
		for file in sorted(listdir(mainFile)):  # Ensure files are also sorted alphabetically
			if file.endswith('.md'):
				filetitle = file.replace('-', ' ').replace('.md', '').capitalize()
				output += f'- [{filetitle}]({mainFile}/{file})  \n'
				total += 1

		print(f'{mainFile} = {directories[mainFile]} files')

print(f'\n{total} total TILs so far\n')

# Write to README.md
with open('README.md', 'w') as file:
	file.write(output)
