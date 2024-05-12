from ansi.color import fg, bg, fx, rgb
from ansi import cursor
class ResetColor:
    def print_cl(self):
        print(self.cl_color)
    def __init__(self):
        self.cl = fg.default+bg.default+fx.normal
        self.name = fg.yellow
        self.warning = fg.boldred
        self.choices = rgb.rgb256(128, 128, 128)
        self.input = fg.cyan
        self.data = fg.yellow
        self.money = fg.brightgreen
color = ResetColor()