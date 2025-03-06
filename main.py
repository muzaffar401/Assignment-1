import streamlit as st
import random
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Guess The Number", page_icon="🔢")

def answer(max: int) -> int:
    return random.randint(1, max)

def init(max: int = 10, pastinit=False, attempts=None):
    if 'max' not in st.session_state:
        st.session_state.max = max
    if 'records' not in st.session_state:
        st.session_state.records = []  # Store game records
    if 'game_won' not in st.session_state:
        st.session_state.game_won = False
    if not pastinit:
        st.session_state.input = 0
        st.session_state.best_score = float('inf')
        st.session_state.cheatcode = 0
    st.session_state.ans = answer(st.session_state.max)
    st.session_state.tries = 0
    st.session_state.over = False
    st.session_state.total = attempts if attempts is not None else float('inf')

def restart():
    difficulty = st.session_state.difficulty
    attempts = None if difficulty == "Easy" else 10 if difficulty == "Medium" else 5
    init(st.session_state.max, pastinit=True, attempts=attempts)
    st.session_state.input += 1
    st.session_state.game_won = False

def main():
    st.title('🎯 Guess the Number')
    st.write("### Welcome to Guess The Number! 🎉\nA random number has been selected. Try to guess it in the fewest attempts possible. Good luck! 😊")
    st.write("---")
    
    if 'ans' not in st.session_state:
        init()
    
    difficulty = st.radio("Select Difficulty:", ["Easy", "Medium", "Hard"], horizontal=True, key='difficulty', on_change=restart)
    attempts = None if difficulty == "Easy" else 10 if difficulty == "Medium" else 5
    
    st.slider('Select Maximum Range ', min_value=10, max_value=1000, value=st.session_state.max, key='max', on_change=restart)
    
    guess = st.number_input('🔢 Enter your Guess', min_value=0, max_value=st.session_state.max, key=st.session_state.input)
    
    if guess == 666 and 666 <= st.session_state.max <= 700:
        st.session_state.cheatcode = 1
    if st.session_state.cheatcode == 1:
        st.info(f'🤫 Cheat Code Activated! The answer is: {st.session_state.ans}')
    
    if guess and not st.session_state.game_won:
        st.session_state.tries += 1
        if attempts is not None:
            st.session_state.total -= 1
        
        if guess < st.session_state.ans and (attempts is None or st.session_state.total > 0):
            st.warning(f'⚠️ {guess} is too low! You have {st.session_state.total if attempts is not None else "∞"} guesses remaining.')
        elif guess > st.session_state.ans and (attempts is None or st.session_state.total > 0):
            st.warning(f'⚠️ {guess} is too high! You have {st.session_state.total if attempts is not None else "∞"} guesses remaining.')
        elif guess == st.session_state.ans:
            if st.session_state.tries < st.session_state.best_score:
                st.session_state.best_score = st.session_state.tries
            
            if not st.session_state.game_won:
                st.session_state.records.append({
                    "Attempts": st.session_state.tries,
                    "Max Range": st.session_state.max,
                    "Difficulty": difficulty
                })
                st.session_state.game_won = True
            
            st.success(f'🎉 {guess} was the right answer! You got it in {st.session_state.tries} attempts! 🏆')
            st.balloons()
            st.session_state.over = True
            st.button('🔄 Play Again!', on_click=restart)
        
        if attempts is not None and st.session_state.total <= 0:
            st.error(f'❌ Game Over! The correct number was {st.session_state.ans}. Try again!')
            st.session_state.over = True
            st.button('🔁 Try Again!', on_click=restart)
    
    st.write("---")
    if st.button('🏆 Show Leaderboard'):
        st.write("### 📊 Game Records")
        if st.session_state.records:
            df = pd.DataFrame(st.session_state.records)
            st.dataframe(df)
            fig = px.bar(df, x='Attempts', y='Max Range', color='Difficulty', barmode='group', title='Game Performance')
            st.plotly_chart(fig)
        else:
            st.info("No games played yet!")
    
    st.metric(label='🥇 Best Score (Least Attempts)', value=st.session_state.best_score if st.session_state.best_score != float('inf') else "N/A")
    st.caption('Made by Muzaffar Ahmed')
    
main()
