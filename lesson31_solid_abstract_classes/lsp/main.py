from player import Player
from captain import Captain

p = Player("Tom")
c = Captain("Jack")

p.set_nick_name("El Tom")
c.set_nick_name("Big Jack")

p.print_info()
c.print_info()
