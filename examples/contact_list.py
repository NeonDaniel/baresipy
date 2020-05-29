from baresipy.contacts import ContactList

db = ContactList()
db.add_contact("joe", "joe@sipxcom.test")
db.search_contact("joe")
db.remove_contact("joe")
db.add_contact("bob", "bob@sipxcom.test")
db.search_contact("bob")
db.update_contact("bob", "me@sipxcom.com")
db.print_contacts()
