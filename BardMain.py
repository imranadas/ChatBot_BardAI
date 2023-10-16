from BardAuth import PSID, PSIDTS, PSIDCC
from tkinterUI import bard_ui

chat_window = bard_ui(PSID, PSIDCC, PSIDTS)
chat_window.mainloop()