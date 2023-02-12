from dataclasses import dataclass, field

from autologging import traced

from src.domain.del_kace import DelKace


@dataclass
@traced
class Snake:
    x: int
    y: int
    dx: int
    dy: int
    deli: list[DelKace] = field(default_factory=list)

    def smer_premika(self, dx: int, dy: int):
        self.dx = dx
        self.dy = dy

    def premikanje(self):
        last_x = self.x
        last_y = self.y
        # premikanje npr.(1,0), desno
        self.x += self.dx
        self.y += self.dy
        for i in range(len(self.deli) - 1, 0, -1):
            self.deli[i].x = self.deli[i - 1].x
            self.deli[i].y = self.deli[i - 1].y
        if self.deli:
            self.deli[0].x = last_x
            self.deli[0].y = last_y

    def dodaj_del_kace(self):
        del_kace = DelKace(x=self.deli[-1].x, y=self.deli[-1].y)
        self.deli.append(del_kace)
