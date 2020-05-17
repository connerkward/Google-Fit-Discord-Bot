"""
Flask Config File
Gets sensitive client (us) auth codes from file
"""
with open("g_auth.txt") as f:
    f.__iter__()
    GOOGLE_CLIENT_ID = f.__next__().strip("\n")
    GOOGLE_CLIENT_SECRET = f.__next__().strip("\n\t")