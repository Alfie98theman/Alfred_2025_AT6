class UserInputValidator:

    #checks a list of strings for valid positive integers
    def validate_positive_integer(self, list_of_strings):
        positive_integers = []
        for integers in list_of_strings:
            if integers.isdigit() and int(integers) > 0:
                positive_integers.append(int(integers))
        return positive_integers

    def validation_message(self, list_of_strings):
        positive_integers = self.validate_positive_integer(list_of_strings)
        print(f"Here are the valid positive integers from your input: {positive_integers}") 