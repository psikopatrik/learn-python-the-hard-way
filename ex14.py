from sys import argv

script, user_name = argv

prompt = '> '

print("Hi {user_name}, I'm the {script} script".format(user_name=user_name, script=script))
print("I'd like to ask you a few questions.")
print("Do you like me {user_name}?".format(user_name=user_name))
likes = input(prompt)

print("Where do you live {user_name}?".format(user_name=user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {likes!r} about liking me.
You live in {lives!r}. Not sure where that is.
And you have a {computer!r} computer. Nice.
""".format(likes=likes, lives=lives, computer=computer))
