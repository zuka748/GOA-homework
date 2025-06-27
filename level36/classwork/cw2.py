def check_vowel(strng, position):
    if position < 0 or position >= len(strng):
        return False
    return strng[position].lower() in 'aeiou'