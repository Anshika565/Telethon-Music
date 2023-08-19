import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN",6699145948:AAFrAfrl1aYgJUnwL-OU0b9433HR1TKrPNI None)
    STRING_SESSION = os.environ.get("STRING_1BVtsOIEBu1cAfEcTr84raRlf_IEb_iUnPFnQg654uW_c4vKDbaB890lfExau3DtH1VoneAEbcr50Jn6_K6aGjbj7x0OEYfc_TGnM4pdLISgnEKfeYREdOr0Ziuso-1IXNS6VoGYYQj3lhZzh3njf1jVzQiIxGy0VLKZR-zCKf86sIZ2efESB2ilCmNq63RfJJS1hs0hs-z4azkEi4fExY_GhPgLPVJjrT6l3s7VsfJ9RnLH6sny2ykxaPpudx31GwJS-U1ugO3lE5X-8tF_kKYNEVD5A4iZWhZuadjo2HBVI4PIeqWgPcWEsIhjmVQjNSvYvTX5vcpUv-ltKHwg1ZDrM6khLq8k=SESSION", None)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
