import streamlit as st
import random

st.title("Number Guessing Game")

if 'secret' not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.max_attempts = 7
    st.session_state.guesses = []
    st.session_state.game_over = False
    st.session_state.won = False

st.write("I have picked a number between **1 and 100**.")
st.write(f"You have **{st.session_state.max_attempts} attempts** to guess it!")

remaining = st.session_state.max_attempts - st.session_state.attempts
st.info(f"Attempts remaining: {remaining}")

if st.session_state.guesses:
    st.write(f"Your guesses: {st.session_state.guesses}")

if not st.session_state.game_over:
    guess = st.number_input(
        "Enter your guess:",
        min_value=1,
        max_value=100,
        step=1
    )

    if st.button("Guess!"):
        st.session_state.attempts += 1
        st.session_state.guesses.append(guess)

        if guess == st.session_state.secret:
            st.success(
                f"CORRECT! You got it in {st.session_state.attempts} guesses!"
            )
            st.session_state.game_over = True
            st.session_state.won = True
        elif guess > st.session_state.secret:
            st.error("Too HIGH! Try lower.")
        else:
            st.warning("Too LOW! Try higher.")

        if (st.session_state.attempts >= st.session_state.max_attempts
                and not st.session_state.won):
            st.error(
                f"GAME OVER! The number was {st.session_state.secret}."
            )
            st.session_state.game_over = True

if st.session_state.game_over:
    if st.button("Play Again"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
