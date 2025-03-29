import sys

instance_type = sys.argv[1]


if instance_type == "t2.micro":
    print("This is free tier")
elif instance_type == "t3.micro":
    print("This will charge you $4")
elif instance_type == "t3.small":
    print("This will charge you $8")
elif instance_type == "t3.medium":
    print("This will charge you $10")
else:
    print("Enter a valid instance type")
