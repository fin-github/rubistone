from random import choice

class Pallete:
    pallete: list[str] = [
        "#5c0f00", # dark
        "#c71212", # brighter
        "#e30909", # normal
        "#e65050", # hi bright
    ]
    
    sorted_pallete: dict[str: list[str]] = {
        "bright": [
            pallete[2], # normal
            pallete[3], # hi bright
        ],
        "dark": [
            pallete[0], # dark
            pallete[1], # brighter
        ]
    }
    
    def random(self):
        return choice(self.pallete)
    
    def rdark(self):
        return choice(self.sorted_pallete["dark"])
    
    def rbright(self):
        return choice(self.sorted_pallete["bright"])
    
pal = Pallete()