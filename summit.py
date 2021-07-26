class Summit:
    def __init__(self, edition, date, participants):
        self.edition = edition
        self.date = date
        self.participants = participants

    def get_message(self):
        with open("message.txt", encoding="utf-8") as f:
            template = f.read()

        participants_string = ""
        for x in range(16):
            if 0 <= x < len(self.participants):
                participants_string += "- " + self.participants[x] + "\n"
            else:
                participants_string += "- \n"

        participants_string += "\nWarteliste:\n"
        if 0 <= 16 < len(self.participants):
            for person in self.participants[16:]:
                participants_string += "- " + person + "\n"
        else:
            participants_string += "- \n"

        return template.format(self.edition, self.date) + participants_string

    def new_participant(self, participant):
        print("Adding participant: " + participant)
        self.participants.append(participant)

    def remove_participant(self, participant):
        print("Removing participant: " + participant)
        self.participants.remove(participant)