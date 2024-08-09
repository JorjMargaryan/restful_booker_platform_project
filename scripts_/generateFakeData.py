import names


class GenerateFakeData:
    def generate_first_name(self):
        """
            This method generates a random first name.
        """
        firstName = names.get_first_name()
        return firstName

    def generate_last_name(self):
        """
            This method generates a random last name.
        """
        lastName = names.get_last_name()
        return lastName

    def generate_gmail(self):
        """
            This method generates a random gmail.
        """
        import random

        # Generate a first and last name
        firstName = self.generate_first_name()
        lastName = self.generate_last_name()

        # Generate a Gmail address
        gmailAddress = f"{firstName.lower()}.{lastName.lower()}{random.randint(1, 100)}@gmail.com"

        return gmailAddress

    def generate_armenian_phone_number(self):
        """
            This method generates a random phone number with country code +374.
        """
        from faker import Faker
        fake = Faker()
        # Country code +374 and 8 digits for the phone number
        localNumber = fake.random_number(digits=8, fix_len=True)
        return f"+374{localNumber}"

    def generate_subject(self):
        """
            This method generates a random subject sentence with approximately 6 words.
        """
        from faker import Faker
        fake = Faker()
        return fake.sentence(nb_words=6)

    def generate_message(self):
        """
            This method generates a random message sentence with approximately 5 sentences.
        """
        from faker import Faker
        fake = Faker()
        return fake.paragraph(nb_sentences=5)

