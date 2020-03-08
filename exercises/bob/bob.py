def response(hey_bob):
    hey_bob = hey_bob.strip()
    if _is_silence(hey_bob):
        return "Fine. Be that way!"
    if _is_shouting(hey_bob) and _is_question(hey_bob):
        return "Calm down, I know what I'm doing!"
    if _is_shouting(hey_bob):
        return "Whoa, chill out!"
    if _is_question(hey_bob):
        return "Sure."
    return "Whatever."


def _is_shouting(hey_bob):
    return hey_bob.isupper()


def _is_question(hey_bob):
    return hey_bob.endswith("?")


def _is_silence(hey_bob):
    return hey_bob == ""
