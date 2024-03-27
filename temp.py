contacts = {
    "Bob": "0777",
    "Rob": "0888"
}

if contacts.get('asdf'):
    print("1")
else:
    print('3')

print(contacts.get('asdf'))

