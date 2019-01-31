#8-13, Python Crash Course, user Profile

#Functions
def build_profile(first, last, **userInfo):
    """Builds a dictionary containing everything we know about a user"""
    profile = {}
    profile["first name"] = first
    profile["last name"] = last
    for key, value in userInfo.items():
        profile[key] = value
    return profile

userProfile = build_profile("Monching", "Copreros",
                            location="house",
                            Complection="handsome")

print(userProfile)
