#Create an empty list of services
services = []

#Populate the list using append or insert
services.append('DynamoDB')
services.append('EC2')
services.append('Lambda')
services.append('S3')
services.append('Neptune')

#Print the list and the length of the list.
print(services)
print(len(services))

#Remove two specific services from the list by name or by index.
services.remove('Lambda')
services.remove('EC2')

#Print the new list and the new length of the list.
print(services)
print(len(services))
