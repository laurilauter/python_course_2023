class Crewmate:
    """Crewmate class."""

    def __init__(self, color: str, role: str, tasks: int = 10):
        """Init the class."""
        self.color = color.capitalize()
        roles = ["Crewmate", "Sheriff", "Guardian Angel", "Altruist"]
        if role in roles:
            self.role = role
        else:
            self.role = "Crewmate"
        self.tasks = tasks
        self.protected = False

    def __repr__(self) -> str:
        """
        Representation of the Crewmate class."""
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        if self.tasks > 0:
            self.tasks -= 1


class Impostor:
    """Crewmate class."""

    def __init__(self, color: str):
        """Init the class."""
        self.color = color.capitalize()
        self.kills = 0

    def __repr__(self) -> str:
        """
        Representation of the Crewmate class."""
        return f"Impostor {self.color}, kills: {self.kills}."


class Spaceship:
    """Crewmate class."""

    def __init__(self):
        """Init the class."""
        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []

    def get_colors(self):
        colors = []
        for crewmate in self.crewmate_list:
            colors.append(crewmate.color)
        for impostor in self.impostor_list:
            colors.append(impostor.color)
        for corpse in self.dead_players:
            colors.append(corpse.color)
        return colors

    def get_crewmate_list(self):
        """Crewmate class."""
        return self.crewmate_list

    def get_impostor_list(self):
        """Crewmate class."""
        return self.impostor_list

    def get_dead_players(self):
        """Crewmate class."""
        return self.dead_players

    def add_crewmate(self, crewmate: Crewmate):
        """Crewmate class."""
        if crewmate in self.crewmate_list or \
                crewmate in self.impostor_list or \
                crewmate in self.dead_players or \
                not hasattr(crewmate, 'role') or \
                crewmate.color in self.get_colors():
            return False
        else:
            self.crewmate_list.append(crewmate)

    def add_impostor(self, impostor: Impostor):
        """Crewmate class."""
        if impostor in self.crewmate_list or \
                impostor in self.impostor_list or \
                impostor in self.dead_players or \
                hasattr(impostor, 'role') or \
                impostor.color in self.get_colors() or \
                len(self.impostor_list) >= 3:
            return False
        else:
            self.impostor_list.append(impostor)

    def kill_impostor(self, sheriff: Crewmate, color: str):
        """Crewmate class."""
        if sheriff.role == "Sheriff":
            for impostor in self.impostor_list:
                if impostor.color == color:
                    self.impostor_list.remove(impostor)
                    self.dead_players.append(impostor)
                else:
                    for crewmate in self.crewmate_list:
                        if crewmate.color == color:
                            self.crewmate_list.remove(sheriff)
                            self.dead_players.append(sheriff)

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        """Crewmate class."""
        if altruist.role == "Altruist":
            for crewmate in self.dead_players:
                if dead_crewmate.color == crewmate.color:
                    self.dead_players.remove(dead_crewmate)
                    self.crewmate_list.append(dead_crewmate)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        """Crewmate class."""
        if guardian_angel.role == "Guardian Angel":
            for crewmate in self.dead_players:
                if crewmate_to_protect.color == crewmate.color:
                    crewmate.protected = True

    def kill_crewmate(self, impostor: Impostor, color: str):
        """Crewmate class."""
        for crewmate in self.crewmate_list:
            if crewmate.color == color:
                if not crewmate.protected:
                    self.crewmate_list.remove(crewmate)
                    self.dead_players.append(crewmate)
                else:
                    crewmate.protected = False

    def sort_crewmates_by_tasks(self):
        """Crewmate class."""
        crewmates_by_tasks = sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)
        return crewmates_by_tasks

    def sort_impostors_by_kills(self):
        """Crewmate class."""
        impostors_by_kills = sorted(self.impostor_list, key=lambda impostor: impostor.kills)
        return impostors_by_kills[::-1]

    def get_regular_crewmates(self):
        """Crewmate class."""
        regulars = []
        for crewmate in self.crewmate_list:
            if crewmate.role == "Crewmate":
                regulars.append(crewmate)
        return regulars

    def get_role_of_player(self, color: str):
        """Crewmate class."""
        for crewmate in self.crewmate_list:
            if color == crewmate.color:
                return crewmate.role

    def get_crewmate_with_most_tasks_done(self):
        """Crewmate class."""
        crewmates_by_tasks = sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)
        return crewmates_by_tasks[0]

    def get_impostor_with_most_kills(self):
        """Crewmate class."""
        impostors_by_kills = sorted(self.impostor_list, key=lambda impostor: impostor.kills)
        return impostors_by_kills[::-1][0]


if __name__ == "__main__":
    print("Spaceship.")
    #
    spaceship = Spaceship()
    print(spaceship.get_dead_players())  # -> []
    print()

    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    white = Crewmate("White", "Impostor")
    yellow = Crewmate("Yellow", "Guardian Angel", tasks=5)
    green = Crewmate("green", "Altruist")
    blue = Crewmate("BLUE", "Sheriff", tasks=0)

    print(red)  # -> Red, role: Crewmate, tasks left: 10.
    print(white)  # -> White, role: Crewmate, tasks left: 10.
    print(yellow)  # -> Yellow, role: Guardian Angel, tasks left: 5.
    print(blue)  # -> Blue, role: Sheriff, tasks left: 0.
    print()

    print("Let's make Yellow complete a task.")
    yellow.complete_task()
    print(yellow)  # ->  Yellow, role: Guardian Angel, tasks left: 4.
    print()

    print("Adding crewmates to Spaceship:")
    spaceship.add_crewmate(red)
    spaceship.add_crewmate(white)
    spaceship.add_crewmate(yellow)
    spaceship.add_crewmate(green)
    print(
        spaceship.get_crewmate_list())  # -> [Red, role: Crewmate, tasks left: 10., White, role: Crewmate, tasks left: 10., Yellow, role: Guardian Angel, tasks left: 4., Green, role: Altruist, tasks left: 10.]

    spaceship.add_impostor(blue)  # Blue cannot be an Impostor.
    print(spaceship.get_impostor_list())  # -> []
    spaceship.add_crewmate(blue)
    print()

    print("Now let's add impostors.")
    orange = Impostor("orANge")
    black = Impostor("black")
    purple = Impostor("Purple")
    spaceship.add_impostor(orange)
    spaceship.add_impostor(black)

    spaceship.add_impostor(Impostor("Blue"))  # Blue player already exists in Spaceship.
    spaceship.add_impostor(purple)
    spaceship.add_impostor(Impostor("Pink"))  # No more than three impostors can be on Spaceship.
    print(spaceship.get_impostor_list())  # -> Orange, Black and Purple
    print()

    print("The game has begun! Orange goes for the kill.")
    spaceship.kill_crewmate(orange, "yellow")
    print(orange)  # -> Impostor Orange, kills: 1.
    spaceship.kill_crewmate(black, "purple")  # You can't kill another Impostor, silly!
    print(spaceship.get_dead_players())  # -> Yellow
    print()

    print("Yellow is a Guardian angel, and can protect their allies when dead.")
    spaceship.protect_crewmate(yellow, green)
    print(green.protected)  # -> True
    spaceship.kill_crewmate(orange, "green")
    print(green in spaceship.dead_players)  # -> False
    print(green.protected)  # -> False
    print()

    print("Green revives their ally.")
    spaceship.kill_crewmate(purple, "RED")
    spaceship.revive_crewmate(green, red)
    print(red in spaceship.dead_players)  # -> False
    print()

    print("Let's check if the sorting and filtering works correctly.")

    red.complete_task()
    print(spaceship.get_role_of_player("Blue"))  # -> Sheriff
    spaceship.kill_crewmate(purple, "blue")
    print(spaceship.sort_crewmates_by_tasks())  # -> Red, White
    print(spaceship.sort_impostors_by_kills())  # -> Purple, Orange, Black
    print(spaceship.get_regular_crewmates())  # -> White, Red
