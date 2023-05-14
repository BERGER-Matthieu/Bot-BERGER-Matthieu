import json
import message_object as msg


class List_chained:
    def __init__(self, first_data):
        self.first_node = Node(None, None, first_data)
        self.last_node = self.first_node
        self.length = 1

    def view(self, index):
        current_node = self.first_node
        i = 0
        while i < index:
            current_node = current_node.following_node
            i += 1
        return current_node.data

    def view_from(self, user):
        current_node = self.first_node
        while current_node.data.user != user:
            current_node = current_node.following_node
        return current_node.data

    def get(self, index):
        current_node = self.first_node
        i = 0
        while i < index:
            current_node = current_node.following_node
            i += 1
        return current_node

    def get_from(self, user):
        current_node = self.first_node
        while current_node.data.user != user:
            current_node = current_node.following_node
        return current_node

    def append(self, data):
        old_last_node = self.last_node
        new_last_node = Node(old_last_node, None, data)
        old_last_node.following_node = new_last_node
        self.last_node = new_last_node
        self.last_node.previous_node = old_last_node
        self.length += 1

    def size(self):
        return self.length

    def clear(self, first_data):
        current_node = self.first_node
        while current_node.following_node is not None:
            current_node = current_node.following_node
            del current_node.previous_node
        del current_node
        self.first_node = Node(None, None, first_data)
        self.last_node = self.first_node
        self.length = 1
        return

    def save(self):
        current_node = self.first_node
        data = {"history": []}
        i = 0

        while i < self.length:
            message = {
                "text": current_node.data.text,
                "user": current_node.data.user
            }
            data["history"].append(message)
            current_node = current_node.following_node
            i += 1

        with open("list.json", "w") as list_json:
            list_json.write(json.dumps(data))
        list_json.close()

        return

    def load(self):
        history_json = json.load(open("list.json", "r"))
        for message in history_json["history"][1:]:
            new_node = msg.Message(message["text"], message["user"])
            self.append(new_node)


class Node:
    def __init__(self, previous_node, following_node, data):
        self.previous_node = previous_node
        self.following_node = following_node
        self.data = data
