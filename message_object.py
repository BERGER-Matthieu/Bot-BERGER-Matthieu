class Message:
    def __init__(self, text, user):
        self.text = text
        self.user = user

    def __str__(self):
        text_str = "%s :\n%s" % (self.user, self.text)
        return text_str
