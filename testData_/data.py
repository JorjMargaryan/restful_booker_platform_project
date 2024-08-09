class UserCredentials:
    """
        This class encapsulates user login information, providing a structured way to store and manage user credentials securely.
        It's designed to enhance code readability, maintainability, and security by centralizing the handling of sensitive login data.
    """
    def __init__(self, username, password):
        """
            Initialize user credentials with the provided username and password.
        """
        self.username = username
        self.password = password


# Valid User Credentials
adminUserData = UserCredentials("admin", "password")

# Correct Description
correctPageDescription = "Welcome to Shady Meadows, a charming Bed & Breakfast nestled in the scenic hills of Newingtonfordburyshire. This beautiful retreat offers a peaceful escape where you’ll feel so at home, you may never want to leave. Each of our rooms is furnished with cozy beds, and we serve a delicious breakfast made with fresh, locally sourced ingredients. Shady Meadows is truly a hidden gem, perfect for a relaxing getaway."

# Restful Booker Platform URL
mainPageUrl = "https://automationintesting.online/"

# Invalid data for form fields
invalidFirstName = "!@#$"
invalidLastName = "#!@#"
invalidEmail = "#@#!#@#"
invalidPhoneNumber = "123"

# Form fields validation messages
firstNameValidationMessages = {
    "required": "First name is required.",
    "length": "First name must be between 2 and 20 characters.",
    "format": "First name can only contain alphabetic characters."
}
lastNameValidationMessages = {
    "required": "Last name is required.",
    "length": "Last name must be between 2 and 20 characters.",
    "format": "Last name can only contain alphabetic characters."
}
nameValidationMessages = {
    "required": "Name is required.",
    "length": "Name must be between 2 and 50 characters.",
    "format": "Name can only contain alphabetic characters."
}
emailValidationMessages = {
    "required": "Email address is required.",
    "format": "Please enter a valid email address (e.g., name@example.com).",
    "uniqueness": "This email address is already in use."
}
phoneValidationMessages = {
    "required": "Phone number is required.",
    "format": "Please enter a valid phone number in the format +374XXXXXXXX.",
    "length": "Phone number must be exactly 12 digits, including the country code."
}
subjectValidationMessages = {
    "required": "Subject is required.",
    "length": "Subject must be between 3 and 100 characters."
}
messageValidationMessages = {
    "required": "Message is required.",
    "length": "Message must be between 10 and 500 characters."
}




