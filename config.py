from pathlib import Path
import tomli_w
import tomllib
import homepage
configFolderDir = Path("~/.config/chunky").expanduser()

def getSpaceDir():
    configDir = Path("~/.config/chunky/config.toml").expanduser()
    if configDir.exists():
        try:
            with open(configDir, "rb") as f:
                data = tomllib.load(f)
            
            return data["spaceDir"]


        except FileNotFoundError:
            return None
        except tomli.TOMLDecodeError:
            return None
    else:
        return None

homepage.configDir = getSpaceDir()

def setSpaceDir(path):
    config = {
        "spaceDir": path
    }
    configFolderDir.mkdir(parents=True, exist_ok=True)

    with open(configFolderDir/ "config.toml", "wb") as f:
        tomli_w.dump(config, f)
    homepage.configDir = path


