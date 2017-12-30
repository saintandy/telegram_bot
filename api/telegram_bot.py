import time


class PrintUtils:
    @staticmethod
    def success(message):
        print("[+] {}".format(message))

    @staticmethod
    def error(message):
        print("[-] {}".format(message))


class TelegramBot:
    def __init__(self, token, authorized_users, known_commands):
        self.token = token
        self.authorized_users = authorized_users
        self.known_commands = known_commands
        self.list = []

    def get_messages(self):
        # you should get all the messages from the token which is `self.token`
        PrintUtils.success("Getting messages")

        # not really the actual message but this should be taken from the link
        message = "This is a message"
        self.list.append(message)

    def send_message(self, user, message):
        PrintUtils.success("Sending message to {}; the message is {}".format(user, message))

    def handle_messages(self):
        PrintUtils.success("Handle messages")
        for message in self.list:
            self.handle_one_message(message)

        self.list = []

    def handle_one_message(self, message):
        PrintUtils.error("Not implemented")

    def run(self):
        PrintUtils.success("Starting bot")

        while True:
            self.get_messages()
            self.handle_messages()
            time.sleep(1)


class SendIPTelegramBot(TelegramBot):
    def handle_one_message(self, message):
        PrintUtils.success("Handling message {}".format(message))

        if message.content not in self.known_commands:
            PrintUtils.error("Unknown command {}".format(message.content))
            return
        elif message.user not in self.authorized_users:
            PrintUtils.error("Unauthorized user {}".format(message.user))
            return

        if message.content == "ip":
            self.send_message(message.user, "5.13.102.102")
        elif message.content == "ping":
            self.send_mesage(message.user, "I'm alive")
