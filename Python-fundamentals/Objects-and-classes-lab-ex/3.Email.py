class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []

email_input = input()

while not email_input == "Stop":
    s, r, c = email_input.split()
    current_email = Email(s, r, c)
    emails.append(current_email)
    email_input = input()

indexes_for_send_mails = [int(index) for index in input().split(", ")]

for send_mail in indexes_for_send_mails:
    email = emails[send_mail]
    email.send()

for email in emails:
    print(email.get_info())