# Import dependencies
import streamlit as st
from utils.interaction import create_questionnaire
from utils.interaction import build_sidebar

def build_header():
    # Title
    st.title("Voice Handicap Index Questionnaire")
    
    # Instructions
    st.subheader("Instructions")
    st.write(
        """
        These are statements many people have used to describe their voices\
        and the effects of their voices on their lives.

        Please select the response that indicates how frequently you have\
        the same experience.
        """
    )
    
    # Reference
    ref_text = "Source: Melbourne ENT Group - Voice Handicap Index (VHI-10)"
    ref_link = "https://melbentgroup.com.au/wp-content/uploads/2015/10/MEG-Voice-Handicap-Index-VHI-10.pdf"
    st.markdown(f"[{ref_text}]({ref_link})")
    

def build_questions():
    # Questions derived from Melbourne ENT Group VHI-10 Questionnaire
    questions = {
        'Question 1': 'My voice makes it difficult for people to hear me',
        'Question 2': 'People have difficulty understanding me in a noisy room',
        'Question 3': 'My voice difficulties restrict my personal & social life',
        'Question 4': 'I feel left out of conversations because of my voice',
        'Question 5': 'My voice problem causes me to lose income',
        'Question 6': 'I feel as though I have to strain to produce voice',
        'Question 7': 'The clarity of my voice is unpredictable',
        'Question 8': 'My voice upsets me',
        'Question 9': 'My voice makes me feel handicapped',
        'Question 10': 'People ask, "What\'s wrong with your voice?"'
    }

    # Define the options
    options = ['Never', 'Almost Never', 'Sometimes', 'Almost Always', 'Always']

    # Use function to create questionnaire
    user_responses = create_questionnaire('vhi', questions, options)  
    

def main():
    build_header()
    build_questions()
    build_sidebar()


if __name__ == '__main__':
    main()