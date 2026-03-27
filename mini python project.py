import random


def play_game():
    secret = random.randint(1, 100)
    max_attempts = 7
    attempts = 0
    guesses = []

    print("=" * 40)
    print("   🎯 NUMBER GUESSING GAME")
    print("=" * 40)
    print("I have picked a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")
    print("=" * 40)

    while attempts < max_attempts:
        remaining = max_attempts - attempts
        print(f"\nAttempts remaining: {remaining}")
        print(f"Your guesses so far: {guesses}")

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("⚠  Please enter a valid number!")
            continue

        if guess < 1 or guess > 100:
            print("⚠  Please enter a number between 1 and 100!")
            continue

        attempts += 1
        guesses.append(guess)

        if guess == secret:
            print("\n" + "=" * 40)
            print(f"🎉 CORRECT! The number was {secret}!")
            print(
                f"✅ You got it in {attempts} guess{'es' if attempts > 1 else ''}!")
            print("=" * 40)
            return True

        elif guess > secret:
            print(f"⬇  Too HIGH! Try something lower.")
        else:
            print(f"⬆  Too LOW! Try something higher.")

    print("\n" + "=" * 40)
    print(f"💀 GAME OVER! The number was {secret}.")
    print("=" * 40)
    return False


def main():
    wins = 0
    losses = 0
    best_score = None

    while True:
        result = play_game()

        if result:
            wins += 1
        else:
            losses += 1

        print(
            f"\n📊 Score — Wins: {wins}  |  Losses: {losses}  |  Best: {best_score if best_score else '—'}")

        again = input("\nPlay again? (yes / no): ").strip().lower()
        if again not in ('yes', 'y'):
            print("\nThanks for playing! Goodbye 👋")
            break
