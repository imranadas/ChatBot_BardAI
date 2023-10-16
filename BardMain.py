from BardAuth import PSID, PSIDTS, PSIDCC
from tkinterUI import bard_ui
from BardAuth import bard_connect

bard = bard_connect()
chat_window = bard_ui(bard)
chat_window.mainloop()