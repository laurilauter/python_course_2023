"""Spaceship."""


class Crewmate:
    """Crewmate class."""

    def __init__(self, color: str, role: str, tasks: int = 10):
        """Init the class."""
        self.color = color.capitalize()
        roles = ["sheriff", "guardian angel", "altruist"]
        if role.lower() in roles:
            self.role = role.title()
        else:
            self.role = "Crewmate"
        self.tasks = tasks
        self.protected = False

    def __repr__(self) -> str:
        """Representation of the Crewmate class."""
        return f"{self.color}, role: {self.role}, tasks left: {self.tasks}."

    def complete_task(self):
        """Crewmate class."""
        if self.tasks > 0:
            self.tasks -= 1


class Impostor:
    """Crewmate class."""

    def __init__(self, color: str):
        """Init the class."""
        self.color = color.capitalize()
        self.kills = 0

    def __repr__(self) -> str:
        """Representation of the Crewmate class."""
        return f"Impostor {self.color}, kills: {self.kills}."


class Spaceship:
    """Crewmate class."""

    def __init__(self):
        """Init the class."""
        self.crewmate_list = []
        self.impostor_list = []
        self.dead_players = []

    def get_colors(self):
        """Init the class."""
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
        color = color.capitalize()
        if sheriff in self.crewmate_list:
            if sheriff.role == "Sheriff":
                # if len(self.impostor_list) > 0:
                if self.get_role_of_player(color) == "Impostor":
                    dead_impostor = self.get_impostor_by_color(color)
                    print("bf not removed", self.impostor_list)
                    self.impostor_list.remove(dead_impostor)
                    print("bf removed", self.impostor_list)
                    self.dead_players.append(dead_impostor)
                    print("bf in dead players", self.dead_players)
                else:
                    for crewmate in self.crewmate_list:
                        if crewmate.color == color:
                            self.crewmate_list.remove(sheriff)
                            self.dead_players.append(sheriff)

    def revive_crewmate(self, altruist: Crewmate, dead_crewmate: Crewmate):
        """Crewmate class."""
        if altruist in self.crewmate_list:
            if altruist.role == "Altruist":
                if dead_crewmate in self.dead_players:
                    self.dead_players.remove(dead_crewmate)
                    self.crewmate_list.append(dead_crewmate)
                    self.crewmate_list.remove(altruist)
                    self.dead_players.append(altruist)

    def protect_crewmate(self, guardian_angel: Crewmate, crewmate_to_protect: Crewmate):
        """Crewmate class."""
        if guardian_angel in self.dead_players:
            if guardian_angel.role == "Guardian Angel":
                if crewmate_to_protect not in self.dead_players:
                    protected = False
                    for crewmate in self.crewmate_list:
                        if crewmate.protected:
                            protected = True
                    if not protected:
                        for mate in self.crewmate_list:
                            if crewmate_to_protect.color == mate.color:
                                if not mate.protected:
                                    mate.protected = True

    def kill_crewmate(self, impostor: Impostor, color: str):
        """Crewmate class."""
        color = color.capitalize()
        if impostor in self.impostor_list:
            for crewmate in self.crewmate_list:
                if crewmate.color == color:
                    if not crewmate.protected:
                        self.crewmate_list.remove(crewmate)
                        self.dead_players.append(crewmate)
                        for imp in self.impostor_list:
                            if imp.color == impostor.color:
                                imp.kills += 1
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

    def get_all_crewmates(self):
        """Crewmate class."""
        all_crewmates = []
        for crewmate in self.crewmate_list:
            all_crewmates.append(crewmate)
        return all_crewmates

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
            if color.capitalize() == crewmate.color:
                return crewmate.role
        for impostor in self.impostor_list:
            if color.capitalize() == impostor.color:
                return "Impostor"

    def get_impostor_by_color(self, color: str):
        if len(self.impostor_list) > 0:
            for impostor in self.impostor_list:
                if impostor.color == color.capitalize():
                    return impostor

    def get_crewmate_with_most_tasks_done(self):
        """Crewmate class."""
        crewmates_by_tasks = sorted(self.crewmate_list, key=lambda crewmate: crewmate.tasks)
        return crewmates_by_tasks[0]

    def get_impostor_with_most_kills(self):
        """Crewmate class."""
        impostors_by_kills = sorted(self.impostor_list, key=lambda impostor: impostor.kills)
        return impostors_by_kills[::-1][0]


if __name__ == "__main__":
    spaceship = Spaceship()
    print("Let's add some crewmates.")
    red = Crewmate("Red", "Crewmate")
    spaceship.add_crewmate(red)
    cyan = Crewmate("cyan", "Sheriff", tasks=0)
    spaceship.add_crewmate(cyan)
    print("All 000", spaceship.get_all_crewmates())
    print("All rrr", spaceship.get_regular_crewmates())

    print()

    print("Now let's add impostors.")
    black = Impostor("black")
    spaceship.add_impostor(black)
    print("All 001", spaceship.get_all_crewmates())
    print("Imps 001", spaceship.get_impostor_list())

    print()
    print("Kill impostor")
    print("Imps before kill b", spaceship.get_impostor_list())
    print("kill imp Black NEXT LINE")
    spaceship.kill_impostor(cyan, "Black")
    print("Imps after kill b", spaceship.get_impostor_list())
    print("Role black", spaceship.get_role_of_player("Black"))
    print("Imps 01", spaceship.get_impostor_list())
    print()
    print("kill imp Red NEXT LINE")
    spaceship.kill_impostor(cyan, "red")
    print("Role red", spaceship.get_role_of_player("red"))
    print("Role cyan", spaceship.get_role_of_player("cyan"))

