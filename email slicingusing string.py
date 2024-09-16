email="abc@gmail.com"
mail=email.index("@")
username=email[0:mid]
domain=email[mid+1]
print(username)
print(domain)
