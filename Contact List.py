def search_contact(contacts, name):
    for contact in contacts:
        contact_name, phone_number = contact.split(',')
        if contact_name.strip() == name:
            return phone_number.strip()


word_pairs = input()

contacts = word_pairs.split()


search_name = input()


phone_number = search_contact(contacts, search_name)


print(phone_number)
