def commands(number):
    events = ["wink", "double blink", "close your eyes", "jump"]
    
    # select events based on the whether NUMBER is written with respective power of two
    handshake = [event for idx, event in enumerate(events) if (number // (2 ** idx)) % 2 == 1]
    handshake = handshake[::-1] if (number // 16) % 2 == 1 else handshake

    return handshake


