from typing import List

class Team:
    def __init__(self) -> None:
        self.members: List[str] = []
        self.index: int = 0
    
    def add_member(self, name: str) -> None:
        self.members.append(name)
    
    def __iter__(self) -> "Team":
        print("__iter__")
        self.index = 0
        return self
    
    def __next__(self) -> str:
        if self.index < len(self.members):
            value = self.members[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration

my_team = Team()
my_team.add_member("Alice")
my_team.add_member("Bob")

for member in my_team:
    print(member)

for member in my_team:
    print(member)