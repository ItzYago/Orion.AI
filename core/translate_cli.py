from actions import Commands


class Translate:

    def __init__(self):

        self.actions = Commands()

        self.commands = {

            "help": self.actions.help,
            "h": self.actions.help,

            "version": self.actions.version,
            "v": self.actions.version,

            "limpar": self.actions.limpar,
            "l": self.actions.limpar,
        }

    def execute(self, command):

        if command in self.commands:
            self.commands[command]()

        else:
            print(
                "Comando desconhecido. Digite 'help'."
            )