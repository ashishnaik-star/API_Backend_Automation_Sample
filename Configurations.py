import configparser


def Configparser():
    confg = configparser.ConfigParser()
    confg.read('Utilities/Properties.ini')
    return confg


def payload_post():
    payload = {
        "title": "Ashish",
        "body": "Message xyz present",
        "userId": 1
    }
    return payload


def payload_put():
    payload = {
        "title": "ashish",
        "body": "naik",
        "userId": 2,
        "id": 5
    }
    return payload


def payload_patch():
    payload = {
        "title": "ashwin"
    }
    return payload
