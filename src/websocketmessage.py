import datetime

def ws_message_enum(type: str):
    types = {"connect", "authorization", "login_success", "login_fail", "ready_to_work", "hash_to_sign", "signed_hash",
             "no_hash_to_sign"}

    if type in types:
        return type
    else:
        raise TypeError("Name of type is incorrect")


wsMessageDefault = {"type": ws_message_enum("connect"), \
                    "contents": str(), \
                    "date": str(datetime.datetime.now())}
