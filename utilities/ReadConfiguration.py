from configparser import ConfigParser


def read_configaration(category, key):
    config = ConfigParser()
    config.read("ConfigrationFile/config.ini")
    return config.get(category, key)


browser = read_configaration("basic info", "browser")
print(browser)

