
# To get USER NAME only out of ARN 

arn = "arn:aws:iam::123456789012:user/johndoe"

print(arn.split("/")[1])
