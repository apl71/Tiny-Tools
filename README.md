# Tiny-Tools

## password

Generate and keep strong passwords.  

### Usage
`$python passwd_gen.py [option] {value}`  
- Show helps:  
`$python passwd_gen.py -h`  
- Specify the length of password:  
`$python passwd_gen.py -l {length}`  
`length` should be an positive integer. The default value is 12.  
- Describe the password:  
`$python passwd_gen.py -s {description}`  
This will append a record like: {description}: {password} in file.  
- Specify the file to keep password:  
`$python passwd_gen.py -p {path}`  
If there is no -p option, it will use default path: ./passwd.txt
