import glob
from pathlib import Path 
from jane.utils import load_plug
import logging
from . import bot 

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

path = "jane/plugins/*.py"
files = glob.glob(path)

for name in files:
  with open(name) as a:
    pxt = Path(a.name)
    plugs = pxt.stem
    load_plug(plugs.replace(".py",""))
print("jane bot has started ")

if __name__ == "__main__":
  bot.run_until_disconnected()