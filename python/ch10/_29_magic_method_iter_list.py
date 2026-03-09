from typing import List, Iterator

class Team:
    def __init__(self) -> None:
        self.members: List[str] = []
        self.index: int = 0
    
    def add_member(self, name: str) -> None:
        self.members.append(name)
    
    def __iter__(self) -> Iterator[str]:
        return iter(self.members)

my_team = Team()
my_team.add_member("Alice")
my_team.add_member("Bob")

for member in my_team:
    print(member)

for member in my_team:
    print(member)