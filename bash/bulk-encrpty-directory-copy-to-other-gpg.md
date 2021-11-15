# Bulk encrypt input directory and copy structure as output

```bash
#!/bin/bash

# The relative path of the file to encrypt, passed as a parameter by find
file_to_encrypt="$1"

# The directory where the mirrored, encrypted directory structure shall end up
dest_dir="$HOME/enc-test/output"

# Relative path to the dir of the file to encrypt, used to create the
# same directory structure elsewhere
dir_of_file_to_encrypt="$(dirname ${file_to_encrypt})"

# In what dir to put the result file, used to be able to create that
# dir before we encrypt the file
dest_dir_of_file_to_encrypt="${dest_dir}/${dir_of_file_to_encrypt}"

# Path to where the encrypted file shall be put
dest_file="${dest_dir}/${file_to_encrypt}"

# To not have to input the password manually each time, put it in this
# file temporarily (make sure to now allow anywone else to access this
# file...)
password_file="$HOME/enc-test/pass.txt"

# Make sure the dest dir exists
mkdir -p "${dest_dir_of_file_to_encrypt}"

echo "About to encrypt ${file_to_encrypt} and putting it in ${dest_file} using password in ${password_file}"
# Encrypt the file and put it in the dest dir
# --symetric: Use simple so called symmetric encryption
# --cipher-algo: Select encryption algorithm
# --passphrase-fd 0: make "password from a file" work
# --yes: Overwrite any existing files
cat "${password_file}" | gpg --symmetric --cipher-algo AES256 --batch --yes --passphrase-fd 0 --yes --output "${dest_file}" "${file_to_encrypt}"
```
