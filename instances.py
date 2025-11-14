from UserInputValidator import UserInputValidator

first_validator = UserInputValidator()
second_validator = UserInputValidator()

list1_of_strings = ["13", "abc", "-13", "1000"]
list2_of_strings = ["45", "hello world", "-12.2", "1"]

print(" The first Validator's results:")
first_validator.validation_message(list1_of_strings)
print("\n The second Validator's results:")
second_validator.validation_message(list2_of_strings)