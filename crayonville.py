# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import time
import base64

LOGGER = get_logger(__name__)

# This is the main function that runs 
def run():
    # Set page config function to center layout
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
        initial_sidebar_state="collapsed",
        layout="centered"
    )

    # Css Styling to set max page width instead of default 730px
    css='''
    <style>
        section.main > div {max-width:680px}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)
    
    # Define function to load an image and set as background
    @st.cache_data
    def get_img(file):
        with open(file, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()

    local_image_path = "./image/paperbackground.jpg" #make sure the image is in the same folder
    img = get_img(local_image_path)

    # Markdown portion to load the background
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{ background-image: url("data:image/png;base64,{img}"); background-size: cover; }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

    # Markdown to style primary buttons
    st.markdown("""
    <style>
    button[kind="primary"] {
    background-color: rgb(240, 103, 137);
    color: rgb(51, 51, 51);
    border: 2px rgb(51, 51, 51);
    height: auto;
    width: 400px;
    padding-top: 10px !important
    padding-bottom: 10px !important;
    }
    </style>""", unsafe_allow_html=True) # Edit this to change the background color and text color

    # Markdown to style secondary buttons
    st.markdown("""
    <style>
    button[kind="secondary"] {
    background-color: rgb(214, 211, 169);
    color: rgb(51, 51, 51);
    border: 2px rgb(51, 51, 51);
    height: auto;
    width: 400px;
    padding-top: 10px !important
    padding-bottom: 10px !important;
    }
    </style>""", unsafe_allow_html=True) # Edit this to change the background color and text color

    if "progress" not in st.session_state:
        st.session_state.progress = 0

    if "answers" not in st.session_state:
        st.session_state.answers = {1:"",
                                    2:"",
                                    3:"",
                                    4:"",
                                    5:"",
                                    6:"",
                                    7:"",
                                    8:"",
                                    9:"",
                                    10:"",
                                    11:"",
                                    12:"",}

    questions = [
        {"landing":"placeholder"},
        {"sign_in":"placeholder"},
        {
            "question": "Q1/12: You're taking the bus on your way back home. It's been a loooong day, what are you thinking about?",
            "image": "image/Q1.gif",
            "answers": {
                "option1": {
                    "text": "I'm just so tired and can't wait to go home. Why does everyday feel the same...",
                    "scores": { "T": 0, "F": 1 },
                },
                "option2": {
                    "text": "Should I rest or work first when I get home? Most importantly, what's for dinner?",
                    "scores": { "T": 1, "F": 0 },
                },
            },
        },
        {
            "question": "Q2/12: You look outside the windows, seems like it's going to rain soon. Suddenly everything turns into darkness!!",
            "image": "image/Q2.gif",
            "answers": {
                "option1": {
                    "text": "I don't remember this tunnel. *Pull out your phone to look at the map*",
                    "scores": { "P": 0, "J": 1 },
                },
                "option2": {
                    "text": "*Turn around to see the other's reaction* Should I ask the driver what's going on?",
                    "scores": { "P": 1, "J": 0 },
                },
            },
        },
        {
            "question": "Q3/12: Before you can do anything, the bus stops and everything around you floats up!",
            "image": "image/Q3.gif",
            "answers": {
                "option1": {
                    "text": "Ok this is weird, am I dreaming? *pinch your arm*",
                    "scores": { "S": 1, "N": 0 },
                },
                "option2": {
                    "text": "Is this a prank? Am I getting kidnapped by aliens?!",
                    "scores": { "S": 0, "N": 1 },
                },
            },
        },
        {
            "question": "Q4/12: Amidst the surprise, your eyes catch something drifting past the window.",
            "image": "image/Q4.gif",
            "answers": {
                "option1": {
                    "text": "Woahhh...so many cats! How cute!! I wanna give them a hug!",
                    "scores": { "T": 0, "F": 1 },
                },
                "option2": {
                    "text": "Cats? In space? That's kinda odd... How do they survive out there?!",
                    "scores": { "T": 1, "F": 0 },
                },
            },
        },
        {
            "question": "Q5/12: 'Welcome Aboard!' a small robot appears and announces, 'We will reach our destination in 5 months 6 days and 2 hours!'",
            "image": "image/Q5.gif",
            "answers": {
                "option1": {
                    "text": "Cool! A space cruise?! Where are we going? Do I get a spacesuit? This is so exciting!",
                    "scores": { "P": 1, "J": 0 },
                },
                "option2": {
                    "text": "Hey uh...Am I in space? How did I get here? When can I go home?! Why..",
                    "scores": { "P": 0, "J": 1 },
                },
            },
        },
        {
            "question": "Q6/12: The robot just points to the back of the bus which now looks more like inside of a spaceship! What do you want to see first?",
            "image": "image/Q6.gif",
            "answers": {
                "option1": {
                    "text": "Solar system themed fountain in the middle. I want to take pictures with it.",
                    "scores": { "I": 0, "E": 1 },
                },
                "option2": {
                    "text": "Cozy corner with a massaging chair. I need to sit down and process.",
                    "scores": { "I": 1, "E": 0 },
                },
            },
        },
        {
            "question": "Q7/12: On the way back to your seat, you are surrounded by cats! 'Unauthorized passenger detected, CAPTURE CAPTURE!'",
            "image": "image/Q7.gif",
            "answers": {
                "option1": {
                    "text": "Woah! What do you mean unauthorized? I'm the passenger of this cruise!",
                    "scores": { "S": 1, "N": 0 }
                },
                "option2": {
                    "text": "Ok, I have no idea what's going on. How about we calm down and chat for a bit?",
                    "scores": { "S": 0, "N": 1 },
                },
            },
        },
        {
            "question": "Q8/12: Suddenly, the robot glides in, it whispers something to the cats that makes them stop.",
            "image": "image/Q8.gif",
            "answers": {
                "option1": {
                    "text": "Bob!! Thank you! You come to save me, right?",
                    "scores": { "E": 1, "I": 0 },
                },
                "option2": {
                    "text": "HA! That's right! Back off, cats! Am I safe to go now?!",
                    "scores": { "E": 0, "I": 1 },
                },
            },
        },
        {
            "question": "Q9/12: The robot transforms into a giant vacuum cleaner, the cats use it to point at you!",
            "image": "image/Q9.gif",
            "answers": {
                "option1": {
                    "text": "Throw your coat at them as distraction, run towards the big green 'EXIT' sign!",
                    "scores": { "J": 1, "P": 0 },
                },
                "option2": {
                    "text": "Run in random direction, confuse them, blend in with the crowd!",
                    "scores": { "J": 0, "P": 1 },
                },
            },
        },
        {
            "question": "Q10/12: You run past the gift shop. Looks like you got rid of them. It wouldn't hurt to get some souvenirs, right?",
            "image": "image/Q10.gif",
            "answers": {
                "option1": {
                    "text": "Get the Jupiter headphone, wear it to hear people's thoughts!",
                    "scores": { "F": 1, "T": 0 },
                },
                "option2": {
                    "text": "Get the Mars watch, turn it and you can time travel!",
                    "scores": { "F": 0, "T": +1 },
                },
            },

        },
        {
            "question": "Q11/12: The giant vacuum cleaner suddenly emerges in front of you! You're sucked into its vortex!!!",
            "image": "image/Q11.gif",
            "answers": {
                "option1": {
                    "text": "It's ok, this is just a dream! I'll wake up soon! *close your eyes and give up*",
                    "scores": { "S": 1, "N": 0 },
                },
                "option2": {
                    "text": "I'll find the way out! Maybe there are some secret doors! *look around for the way out*",
                    "scores": { "S": 0, "N": 1 },
                },
            },
        },
        {
            "question": "Q12/12: After a moment of darkness, you find yourself back in the bus. 'Are you alright?' the ticket inspector asks",
            "image": "image/Q12.gif",
            "answers": {
                "option1": {
                    "text": "Woah! I thought I was captured... Nevermind! I'm alright now, I guess? *panic in silence*",
                    "scores": { "E": 0, "I": 1 },
                },
                "option2": {
                    "text": "You won't believe it...I think I just had the wildest dream ever! *tell him about your space adventure*",
                    "scores": { "E": 1, "I": 0 },
                },
            },
        },
        {
            "question": "When you look up again, the inspector's already gone. You glance outside the window, darkness creeps in as the bus enters another tunnel...",
            "image": "image/Q13.gif",
            "answers": {
                "option1": {
                    "text": "Wait...was that Bob?",
                },
                "option2": {
                    "text": "Oh no...Do I have to go through this again?",
                },
            },
        },
    ]

    resultOptions = {
        "ISTJ": {
            "image": "1DE.png",
        },
        "ISFJ": {
            "image": "2light.png"
        },
        "INFJ": {
            "image": "3UFO.png"
        },
        "INTJ": {
            "image": "4nebula.png"
        },
        "ISTP": {
            "image": "5comet.png"
        },
        "ISFP": {
            "image": "6ST.png"
        },
        "INFP": {
            "image": "7DM.png"
        },
        "INTP": {
            "image": "8met.png"
        },
        "ESTP": {
            "image": "9BH.png"
        },
        "ESFP": {
            "image": "10Sn.png"
        },
        "ENFP": {
            "image": "11Grav.png"
        },
        "ENTP": {
            "image": "12hand.png"
        },
        "ESTJ": {
            "image": "13sat.png"
        },
        "ESFJ": {
            "image": "14sun.png"
        },
        "ENFJ": {
            "image": "15gal.png"
        },
        "ENTJ": {
            "image": "16rocket.png"
        },
    }

    # Go through all the scores and find the personality
    def calculate_results(answers):
        result = {}
        personality = ""
        for answer in answers.keys():
            for attribute in answers[answer].keys():
                if attribute not in result.keys():
                    result.update({attribute:answers[answer][attribute]})
                else:
                    result[attribute] = result[attribute] + answers[answer][attribute]

        if result["I"] > result["E"]:
            personality += "I"
        else:
            personality += "E"
        if result["N"] > result["S"]:
            personality += "N"
        else:
            personality += "S"
        if result["T"] > result["F"]:
            personality += "T"
        else:
            personality += "F"
        if result["P"] > result["J"]:
            personality += "P"
        else:
            personality += "J"

        return personality

    def show_gif(filepath):
        """### gif from local file"""
        file_ = open(filepath, "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" width="400" height="400" alt="gif">',
            unsafe_allow_html=True,
        )

    if st.session_state.progress == 0:
        # left_co, cent_co,last_co = st.columns(3)
        # with cent_co:
        # st.title("Welcome to Crayonville!")
        # show_gif("./image/main.gif")
        st.image("./image/hagridlogo.png", width=600) #Change this line to show the logo
        left_col, cent_col, right_col = st.columns(3)
        with cent_col:
            if st.button("Start!", type="primary"):
                    st.session_state.progress = 1
                    st.rerun()

            
    elif st.session_state.progress == 1:
        # left_co, cent_co,last_co = st.columns(3)
        # with cent_co:
        st.write("Step 1: Click on the link and fill up the form sg")
        st.image("./image/qrcode.png", width=400) # Change here to show qrcode image
        st.write("www.abcdef.com") # Change here to show your link
        st.write("Step 2: You will receive an email with the code after you have completed the form sg")
        password = st.text_input("Step 3: Enter the code from your email!")
        if st.button("Start Personality Quiz", type="primary"):
            if password == "whatismycolour": # Change here to set the password
                st.session_state.progress = 2
                st.rerun()
            else:
                st.write("The code is incorrect")
    
    elif st.session_state.progress > 13: # Change the number here based on the number of questions. Set as 13 for 12 questions
        # left_co, cent_co,last_co = st.columns(3)
        # with cent_co:
        st.progress(100, "Completed")
        st.write("Completed!")
        personality = calculate_results(st.session_state.answers)
        st.write(personality)
        st.image("image/"+resultOptions[personality]['image'], width=400)
        # show_gif("image/"+resultOptions[personality]['image'])
        # st.write(resultOptions[personality]['image'])
        left_btn, center_btn, right_btn = st.columns(3)
        with left_btn:
            if st.button("Restart Personality Quiz", type="secondary"):
                st.session_state.progress = 2
                st.rerun()
        with center_btn:
            st.link_button("E-learning", "https://www.google.com", type="links") # Edit here for the e-learning website
        with right_btn:
            st.link_button("Inno-portal", "https://www.google.com", type="links") # Edit here for the inno-portal website


        

    else:
        # left_co, cent_co,last_co = st.columns(3)
        # with cent_co:
        st.progress((st.session_state.progress-1)*8, text="Progress")
        st.write(questions[st.session_state.progress]['question'])
        # st.image(questions[st.session_state.progress]['image'])
        show_gif(questions[st.session_state.progress]['image'])
        # st.write(questions[st.session_state.progress]['image']) # Write image name for now instead of showing image
        time.sleep(0.5)
        if st.button(questions[st.session_state.progress]['answers']['option1']['text'], type="primary"):
            st.session_state.answers[st.session_state.progress-1] = questions[st.session_state.progress]['answers']['option1']['scores']
            st.session_state.progress = st.session_state.progress + 1
            st.rerun()
        if st.button(questions[st.session_state.progress]['answers']['option2']['text'], type="primary"):
            st.session_state.answers[st.session_state.progress-1] = questions[st.session_state.progress]['answers']['option2']['scores']
            st.session_state.progress = st.session_state.progress + 1
            st.rerun()
        if st.button("Previous Question", type="secondary"):
            if st.session_state.progress > 1:
                st.session_state.progress = st.session_state.progress - 1
                st.rerun()
            else:
                st.session_state.progress = 0
                st.rerun()

if __name__ == "__main__":
    run()
