words = ['cat', 'window', 'defenestrate']

for w in words:
    print(w, len(w))
# sayying = input("what")

# if sayying 

users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
for user, status in users.copy().items():
    if status == "active":
        del users[user]


for user, status in users.items():
        print(user)

