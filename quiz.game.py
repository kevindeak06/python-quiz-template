# --- DATA SETUP ---
# Using tuples for static data (questions & options) that won't change
questions = ("1. Melyik állat ugat? ",
             "2. Hány lába van egy póknak? ",
             "3. Melyik állat a dzsungel királya? ",
             "4. Mit eszik főként az óriáspanda? ",
             "5. Melyik madár nem tud repülni az alábbiak közül? ")

options = (("A) Macska", "B) Kutya", "C) Ló"),
           ("A) 4", "B) 6", "C) 8"),
           ("A) Oroszlán", "B) Tigris", "C) Elefánt"),
           ("A) Húst", "B) Halat", "C) Bambuszt"),
           ("A) Sas", "B) Pingvin", "C) Veréb"))

# Correct answers key and valid input options
answers = ["B", "C", "A", "C", "B"]
possible_answers = ["A", "B", "C"]

# --- GAME VARIABLES ---
question_number = 0
guesses = []
points = 0

# --- MAIN GAME LOOP ---
for question in questions:
    print("-----------------------")
    print(question)
    # Display options corresponding to the current question
    print(options[questions.index(question)])
    print()

    # Get user input
    guess = input("Válasz: ").upper()
    guesses.append(guess)

    # --- INPUT VALIDATION ---
    # Ensure the user enters a valid option (A, B, or C)
    while guess not in possible_answers:
        print("Kérlek a kérdésre válaszolj! (A,B,C)! ")
        # Remove the invalid guess from the list before asking again
        guesses.remove(guess)
        guess = input("Válasz: ").upper()
        # Add the new (potentially valid) guess
        guesses.append(guess)

    # --- SCORING LOGIC ---
    if guesses[question_number] == answers[question_number]:
       print("Helyes! ")
       question_number += 1
       points += 1
    elif guesses[question_number] != answers[question_number]:
       print(f"Helytelen válasz! Helyes válasz: {answers[question_number]}")
       question_number += 1

# --- RESULTS DISPLAY ---
print("-----------------------")
print("        VÁLASZOK")
print("-----------------------")

print("A megoldások: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("A válaszaid:  ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

print("-----------------------")
print("        PONTSZÁM")
print("-----------------------")

# Calculate final percentage
points = (points / question_number) * 100
print(f"         {points:.0f}%!")

print()