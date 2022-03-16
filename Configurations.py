import configparser


def Configparser():
    confg = configparser.ConfigParser()
    confg.read('Utilities/Properties.ini')
    return confg

