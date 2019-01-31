#Using Arbitray keywords as arguements

def build_profile(first, last, **userInfo):
    """Builds a dictionary containing everything we know about a user"""
    profile = {}
    profile["first name"] = first
    profile["last name"] = last
    for key, value in userInfo.items():
        profile[key] = value
    return profile

userProfile = build_profile("albert", "einstein",
                            location= 'princeton',
                            field= 'physics')

print(userProfile)
