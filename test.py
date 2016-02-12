from germanium.static import *
from time import sleep

open_browser()
go_to("http://localhost:9000")
type_keys("/etc/passwd", Input("fname"))
sleep(5)
close_browser()

