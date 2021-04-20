from cipher import Cipher

def test_encrypt_caesar_gives_empty_str_without_text():
    cipher = Cipher()
    code = cipher.encrypt_caesar(" ", -3)
    assert code == " "

def test_encrypt_caesar_lower_case():
    cipher = Cipher()
    code = cipher.encrypt_caesar("abcde", 2)
    assert code == "cdefg"

def test_encrypt_caesar_upper_case():
    cipher = Cipher()
    code = cipher.encrypt_caesar("XYZ", 4)
    assert code == "BCD"

def test_encrypt_caesar_works_for_a_sentence():
    cipher = Cipher()
    code = cipher.encrypt_caesar("Hello how are you today", 5)
    assert code == "Mjqqt mtb fwj dtz ytifd"

def test_encrypt_caesar_works_if_numbers_is_in_a_string():
    cipher = Cipher()
    code = cipher.encrypt_caesar("abcABC123xyzXYZ", 2)
    assert code == "cdeCDE123zabZAB"

def test_encrypt_caesar_special_characters_dont_change():
    cipher = Cipher()
    code = cipher.encrypt_caesar("?*£$%^", 5)
    assert code == "?*£$%^"

def test_encrypt_caesar_negative_shift():
    cipher = Cipher()
    code = cipher.encrypt_caesar("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", -3)
    assert code == "QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD"
