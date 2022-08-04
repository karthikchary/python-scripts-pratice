devops=["jenkins","Ansible","Docker","Terraform"]
development=("NodeJs","Angular","Python")

user_skill = input("Enter your desired skill type: ")
print(user_skill)
if user_skill in devops:
    print("skill in Devops team")
elif user_skill in development:
    print("skill in development team")
else:
    print("skill not present")