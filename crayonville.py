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

#import streamlit as library
#then you can import all the functions
import streamlit as st
from streamlit.logger import get_logger
import time
import base64
import streamlit.components.v1 as components

#dont know what this do it is auto generated when you create the streamlit app
LOGGER = get_logger(__name__)

# This is the main function that runs 
def run():
    # Set page config function to center layout
    st.set_page_config(
        page_title="Hagrid and the Yellow Crayon",
        page_icon="🖍️",
        initial_sidebar_state="collapsed",
        layout="centered"
    )

    # Css Styling to set max page width instead of default 730px
    css='''
    <style>
        section.main > div {max-width:600px}
    </style>
    '''
    st.markdown(css, unsafe_allow_html=True)
    st.markdown("""
        <style>
               .block-container {
                    padding-top: 1rem;
                    padding-bottom: 2rem;
                    padding-left: 1rem;
                    padding-right: 1rem;
                }
        </style>
        """, unsafe_allow_html=True) # Set this to edit the top padding
    
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

    # # st.markdown(""" 
    # <style> 
    # button[kind="primary"] { 
    # background-color: #EDBB09;
    # color: rgb(51, 51, 51); 
    # border: 2px rgb(51, 51, 51); 
    # height: auto; 
    # width: 600px; 
    # } 
    # button[kind="primary"]:hover { 
    # # background-color: rgb(250, 180, 197); 
    # color: rgb(51, 51, 51); 
    # border: rgb(51, 51, 51); 
    # } 
    # button[kind="primary"]:active { 
    # # background-color: rgb(250, 180, 197); 
    # color: rgb(51, 51, 51) !important; 
    # border: rgb(51, 51, 51); 
    # } 
    # button[kind="primary"]:focus { 
    # # background-color: rgb(250, 180, 197); 
    # color: rgb(51, 51, 51) !important; 
    # border: rgb(51, 51, 51); 
    # } 
    # button[kind="primary"]:visited { 
    # # background-color: rgb(255, 217, 115); 
    # color: rgb(51, 51, 51) !important; 
    # border: rgb(51, 51, 51); 
    # } 
     
    # button[kind="secondary"] { 
    # background-color: #EDBB015); 
    # color: rgb(51, 51, 51); 
    # border: 2px rgb(51, 51, 51); 
    # height: auto; 
    # width: 400px; 
    # } 
    # button[kind="secondary"]:hover { 
    # # background-color: rgb(255, 233, 173); 
    # color: rgb(51, 51, 51); 
    # border: rgb(51, 51, 51); 
    # } 
    # button[kind="secondary"]:active { 
    # # background-color: rgb(255, 233, 173); 
    # color: rgb(51, 51, 51) !important; 
    # border: rgb(51, 51, 51); 
    # } 
    # button[kind="secondary"]:focus { 
    # # background-color: rgb(255, 233, 173); 
    # color: rgb(51, 51, 51) !important; 
    # border: rgb(51, 51, 51); 
    # } 
     
    # a[kind="primary"] { 
    # background-color: #EDBB05); 
    # color: rgb(51, 51, 51) !important; 
    # border: 2px rgb(51, 51, 51); 
    # height: auto; 
    # width: 200px; 
    # padding-top: 10px !important 
    # padding-bottom: 10px !important; 
    # } 
    # a[kind="primary"]:hover { 
    # # background-color: rgb(255, 233, 173); 
    # color: rgb(51, 51, 51) !important; 
    # border: rgb(51, 51, 51); 
    # } 
    # a[kind="primary"]:active { 
    # # background-color: rgb(140, 139, 105); 
    # color: rgb(51, 51, 51) !important; 
    # border: rgb(51, 51, 51); 
    # } 
    # a[kind="primary"]:focus { 
    # # background-color: rgb(140, 139, 105); 
    # color: rgb(51, 51, 51) !important; 
    # border: rgb(51, 51, 51); 
    # } 
    # """, unsafe_allow_html=True)
    
    # Markdown to style primary buttons
    st.markdown("""
    <style>
    button[kind="primary"] {
    background-color: #EDBB09;
    color: rgb(51, 51, 51);
    border: 2px rgb(51, 51, 51);
    height: auto;
    width: 270px !important;
    padding-top: 10px !important
    padding-bottom: 10px !important;
    margin-left: 25%;
    }
    button[kind="primary"]:hover { 
    background-color: #EDBB09; 
    color: rgb(51, 51, 51); 
    border: rgb(51, 51, 51); 
    } 
    </style>""", unsafe_allow_html=True) # Edit this to change the background color and text color

    # Markdown to style secondary buttons
    st.markdown("""
    <style>
    button[kind="secondary"] {
    background-color: #EDBB09;
    color: rgb(51, 51, 51);
    border: 2px rgb(51, 51, 51);
    height: auto;
    width: 600px !important;
    padding-top: 10px !important
    padding-bottom: 10px !important;
    margin: 0 auto;
    }
    button[kind="secondary"]:hover { 
    background-color: #EDBB09; 
    color: rgb(51, 51, 51); 
    border: rgb(51, 51, 51); 
    } 
    button[kind="secondary"]:focus { 
    background-color: #EDBB09; 
    color: rgb(51, 51, 51); 
    border: rgb(51, 51, 51); 
    } 
    </style>""", unsafe_allow_html=True) # Edit this to change the background color and text color

    st.markdown("""
    <style>
    div[data-baseweb="base-input"]{
    background-color: rgb(240, 229, 191);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
    div[data-testid="InputInstructions"] > span:nth-child(1) {
    visibility: hidden;
    }
    </style>""", unsafe_allow_html=True)

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
                                    12:"",
                                    13:"",
                                    14:"",
                                    15:"",}

    questions = [
        {"landing":"placeholder"},
        {"sign_in":"placeholder"},
        {
            "question": "Q1/15: You stumbled upon a torn map leading to the legendary Wizard Hagrid. What's your move?",
            "image": "image/Q1.png",
            "answers": {
                "option1": {
                    "text": "Search frantically for the missing piece.",
                    "scores": { "Red": 1, "Blue": 0 },
                },
                "option2": {
                    "text": "Craft a clever plan without the missing piece.",
                    "scores": { "Red": 0, "Blue": 1 },
                },
            },
        },
        {
            "question": "Q2/15: Suddenly, you looked ahead and spotted a colourful boat along a rainbow river.",
            "image": "image/Q2.png",
            "answers": {
                "option1": {
                    "text": "Imagine an epic boat adventure and gather supplies.",
                    "scores": { "Blue": 1, "White": 0 },
                },
                "option2": {
                    "text": "Inspect the boat's construction and durability for the journey.",
                    "scores": { "Blue": 0, "White": 1 },
                },
            },
        },
        {
            "question": "Q3/15: You decided to take the boat and it sailed into a mysterious cave. You thought to yourself:",
            "image": "image/Q3.png",
            "answers": {
                "option1": {
                    "text": "Wow, what a majestic cave. I wonder what I can discover here.",
                    "scores": { "Yellow": 1, "Green": 0 },
                },
                "option2": {
                    "text": "This looks like a safe space for me to hide and take shelter.",
                    "scores": { "Yellow": 0, "Green": 1 },
                },
            },
        },
        {
            "question": "Q4/15: Amidst hunger, you discover a mushroom in the cave. You thought:",
            "image": "image/Q4.png",
            "answers": {
                "option1": {
                    "text": "I don’t feel too good about this mushroom. Will skip it.",
                    "scores": { "Red": 1, "Black": 0 },
                },
                "option2": {
                    "text": "This mushroom will very likely kill me! ",
                    "scores": { "Red": 0, "Black": 1 },
                },
            },
        },
        {
            "question": "Q5/15: You walked along the cave and spotted some graffiti on the walls. You wonder:",
            "image": "image/Q5.png",
            "answers": {
                "option1": {
                    "text": "I should decipher what the grafitti means before I decide if I should take it seriously.",
                    "scores": { "Blue": 1, "Yellow": 0 },
                },
                "option2": {
                    "text": "A clue! Getting closer to the Wizard Hagrid.",
                    "scores": { "Blue": 0, "Yellow": 1 },
                },
            },
        },
        {
            "question": "Q6/15: Suddenly, you noticed a rabbit outside the cave waving at you. It gestured for you to follow it. Your immediate reaction:",
            "image": "image/Q6.png",
            "answers": {
                "option1": {
                    "text": "Look at rabbit sceptically and wonder if following it will be a huge risk.",
                    "scores": { "Black": 1, "White": 0 },
                },
                "option2": {
                    "text": "Examine the rabbit's behaviour and its surroundings before making a decision.",
                    "scores": { "Black": 0, "White": 1 },
                },
            },
        },
        {
            "question": 'Q7/15: "If you want food, go to the Enchanted Forest!" the rabbit shouted and ran off. You decided to head to the Enchanted Forest, where you found yourselves surrounded by fruit trees. You thought:',
            "image": "image/Q7.png",
            "answers": {
                "option1": {
                    "text": "Just nice! I feel super hungry!",
                    "scores": { "Red": 1, "White": 0 }
                },
                "option2": {
                    "text": "If the birds are enjoying them, it should be safe for me too.",
                    "scores": { "Red": 0, "White": 1 },
                },
            },
        },
        {
            "question": "Q8/15: After eating the fruits, you were transported instantly to Mount Chroma. You met a little paintbrush who said 'Are you looking for Wizard Hagrid? I can bring you there.' You:",
            "image": "image/Q8.png",
            "answers": {
                "option1": {
                    "text": "I'm incredibly lucky to have a guide like you!",
                    "scores": { "Yellow": 1, "Black": 0 },
                },
                "option2": {
                    "text": "Can I trust him? What if this is a trap?",
                    "scores": { "Yellow": 0, "Black": 1 },
                },
            },
        },
        {
            "question": "Q9/15: You followed the little paintbrush to a cylindrical house. When the door opens, you were greeted by a group of colourful little paintbrushes. You thought:",
            "image": "image/Q9.png",
            "answers": {
                "option1": {
                    "text": "I should first ask them who they are before I share about my plans.",
                    "scores": { "Blue": 1, "Green": 0 },
                },
                "option2": {
                    "text": "Maybe they will bring me to Wizard Hagrid through a secret route in their house!",
                    "scores": { "Blue": 0, "Green": 1 },
                },
            },
        },
        {
            "question": "Q10/15: ‘I challenge you to a game of ‘Drawasaurus’. If you can draw faster than us, we’ll show you the way to Wizard Hagrid. If you are slower, you’ll give up your colour to us,’ said the paintbrushes.",
            "image": "image/Q10.png",
            "answers": {
                "option1": {
                    "text": "I sense that I might be able to draw faster than these little paintbrushes.",
                    "scores": { "Red": 1, "Yellow": 0 },
                },
                "option2": {
                    "text": "Game on! One crayon offers better control and precision than a group of paintbrushes anyway.",
                    "scores": { "Red": 0, "Yellow": 1 },
                },
            },

        },
        {
            "question": "Q11/15: You drew as frantically as you could, determined to win. You notice that the paintbrushes couldn’t keep up with you.",
            "image": "image/Q11.png",
            "answers": {
                "option1": {
                    "text": "Looks like they’re making a mess painting together. I’m definitely going to win.",
                    "scores": { "White": 1, "Yellow": 0 },
                },
                "option2": {
                    "text": "Woohoo! I knew it! Too many paintbrushes spoil the drawing. It’s good to operate alone!",
                    "scores": { "White": 0, "Yellow": 1 },
                },
            },
        },
        {
            "question": "Q12/15: Defeated that they had lost, the paintbrushes pointed you to the long road ahead, which leads to the art gallery. They said that Wizard Hagrid lives there. You:",
            "image": "image/Q12.png",
            "answers": {
                "option1": {
                    "text": "Sense that I am getting closer to my destination this time. ",
                    "scores": { "Red": 1, "Green": 0 },
                },
                "option2": {
                    "text": "Wonder if there are shorter paths to get to Wizard Hagrid. ",
                    "scores": { "Red": 0, "Green": 1 },
                },
            },
        },
        {
            "question": "Q13/15: You decided to follow the road towards the art gallery. Entering the art gallery, you saw a wise old man, who turns out to be Wizard Hagrid that you’ve been looking for. You:",
            "image": "image/Q13.png",
            "answers": {
                "option1": {
                    "text": "Eagerly prepare the things you intend to say to Wizard Hagrid. ",
                    "scores": { "Blue": 1, "Black": 0 },
                },
                "option2": {
                    "text": "Scrutinize Wizard Hagrid, wondering if he is truly powerful.",
                    "scores": { "Blue": 0, "Black": 1 },
                },
            },
        },
        {
            "question": "Q14/15: You say, ‘I want to be a super crayon as I wish to create beautiful art’. \n ‘And I see you’ve come a long way to meet me. I shall grant you your wishes, but you need to give up who you are to be a new crayon.’ Said Wizard Hagrid. ",
            "image": "image/Q14.png",
            "answers": {
                "option1": {
                    "text": "Given the time, effort and sacrifices I have made, and the reputation of this Wizard, it makes sense for me to listen to him.",
                    "scores": { "White": 1, "Green": 0 },
                },
                "option2": {
                    "text": "Can’t wait to see the new me!",
                    "scores": { "White": 0, "Green": 1 },
                },
            },
        },
        {
            "question": "Q15/15: ‘Now, pick the picture that resonates with you. It will reveal your destiny,’ said Wizard Hagrid. You: ",
            "image": "image/Q15.png",
            "answers": {
                "option1": {
                    "text": "Cautiously examine each picture, pondering its impact...",
                    "scores": { "Black": 1, "Green": 0 },
                },
                "option2": {
                    "text": "Head straight to your desired picture, buzzing with excitement on the ideas that might happen. ",
                    "scores": { "Black": 0, "Green": 1 },
                },
            },
        },
    ]

    resultOptions = {
        frozenset(["White", "Black"]): {
            "image": "groundedgrey.png",
        },
        frozenset(["White", "Yellow"]): {
            "image": "curiouscream.png"
        },
        frozenset(["White", "Green"]): {
            "image": "methodicalmint.png"
        },
        frozenset(["White", "Blue"]): {
            "image": "adaptiveaqua.png"
        },
        frozenset(["White", "Red"]): {
            "image": "pragmaticpink.png"
        },
        frozenset(["Black", "Yellow"]): {
            "image": "mindfulmustard.png"
        },
        frozenset(["Black", "Green"]): {
            "image": "farsightedforest.png"
        },
        frozenset(["Black", "Blue"]): {
            "image": "navigationalnavy.png"
        },
        frozenset(["Black", "Red"]): {
            "image": "meticulousmaroon.png"
        },
        frozenset(["Yellow", "Green"]): {
            "image": "luminouslime.png"
        },
        frozenset(["Yellow", "Blue"]): {
            "image": "tenaciousturquoise.png"
        },
        frozenset(["Yellow", "Red"]): {
            "image": "optimisticorange.png"
        },
        frozenset(["Green", "Blue"]):  {
            "image": "trailblazingteal.png"
        },
        frozenset(["Green", "Red"]): {
            "image": "boldbrown.png"
        },
        frozenset(["Blue", "Red"]): {
            "image": "perceptivepurple.png"
        },
        
    }

    # Go through all the scores and find the personality
    def calculate_results(answers):
        result = {}
        # personality = ""
        for question_number in answers.keys():
            for colour in answers[question_number].keys():
                if colour not in result.keys():
                    result.update({colour:answers[question_number][colour]})
                else:
                    result[colour] = result[colour] + answers[question_number][colour]

        result = sorted(result.items(), key=lambda item: item[1], reverse=True)
        result = [k for k,v in result]
        personality = frozenset(result[:2])
        # if result["I"] > result["E"]:
        #     personality += "I"
        # else:
        #     personality += "E"
        # if result["N"] > result["S"]:
        #     personality += "N"
        # else:
        #     personality += "S"
        # if result["T"] > result["F"]:
        #     personality += "T"
        # else:
        #     personality += "F"
        # if result["P"] > result["J"]:
        #     personality += "P"
        # else:
        #     personality += "J"

        return personality

    def show_gif(filepath):
        """### gif from local file"""
        file_ = open(filepath, "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()

        st.markdown(
            f'<img src="data:image/gif;base64,{data_url}" width="400" alt="gif" style="display: block; margin: 0 auto;">',
            unsafe_allow_html=True,
        )

    if st.session_state.progress == 0:
        # left_co, cent_co,last_co = st.columns(3)
        # with cent_co:
        # st.title("Welcome to Crayonville!")
        # show_gif("./image/main.gif")
        st.image("./image/hagridlogo1.png", use_column_width=True) #Change this line to show the logo
        st.markdown('<div style="text-align:center; font-size:18px;">Embark on an exciting adventure as a crayon with big dreams!</div>', unsafe_allow_html=True)
        st.markdown('<div style="text-align:center; font-size:18px;">Join the quest to find the legendary Wizard Hagrid and unlock your super powers to create magnificent art.</div>', unsafe_allow_html=True)
        st.markdown("") # Empty text to act as spacing
        if st.button("Start!", type="primary"):
                st.session_state.progress = 1
                st.rerun()

            
    elif st.session_state.progress == 1:
        st.markdown('<div style="font-size:20px;"><b>Step 1:</b> Click on the link and fill up the FormSG</div>', unsafe_allow_html=True)
        #st.image("./image/qrcode.png", width=400) # Change here to show qrcode image
        st.write("https://go.gov.sg/crayonvilleregistration") # Change here to show your link
        st.markdown('<div style="font-size:20px;"><b>Step 2:</b> You will receive an email with the code after you have completed the FormSG</div>', unsafe_allow_html=True)
        st.markdown('') # Empty string for spacing
        st.markdown('<div style="font-size:20px;"><b>Step 3:</b> Enter the code from your email!</div>', unsafe_allow_html=True)
        password = st.text_input('', label_visibility='collapsed')

        if st.button("Start Personality Quiz", type="primary"):
            if password == "thedayiknowmycolour": # Change here to set the password
                st.session_state.progress = 2
                st.rerun()
            else:
                st.write("The code is incorrect")
    
    elif st.session_state.progress == 17:
        st.markdown('<div style="font-size:20px;"> Before you discover <b>your personalised crayon profiles...</b> </div>', unsafe_allow_html=True)
        #st.image("./image/qrcode.png", width=400) # Change here to show qrcode image
        if st.button("See my profile", type="primary"):
                st.session_state.progress += 1
                st.rerun()

    elif st.session_state.progress > 17: # Change the number here based on the number of questions. Set as 13 for 12 questions
        # left_co, cent_co,last_co = st.columns(3)
        # with cent_co:
        
        #st.write(st.session_state.answers)
        st.markdown('<div style="font-size:20px;"><b>Completed!</b></div>', unsafe_allow_html=True)
        st.progress(100)
        # st.write("Completed!")
        personality = calculate_results(st.session_state.answers)
        # st.markdown(f'<div style="font-size:20px;"><b>{personality}</b></div>', unsafe_allow_html=True)
        # st.write(personality)
        left_img, cent_img, right_img = st.columns([1,4,3])
        with cent_img:
            st.image("image/"+resultOptions[personality]['image'], width=400)
        # show_gif("image/"+resultOptions[personality]['image'])
        # st.write(resultOptions[personality]['image'])
        left_btn, right_btn = st.columns(2)

        with left_btn:
            st.markdown("")
            st.link_button("Learn about Design Thinking Tools", "https://www.google.com", use_container_width=True) # Edit here for E-learning website
            # st.markdown("") # Empty string for spacing
            # st.link_button("Check out the other profiles", "https://www.google.com", use_container_width=True) # Edit here for E-learning website
        with right_btn:
            # st.link_button("Design Thinking E-Learning", "https://www.google.com", use_container_width=True) # Edit here for the inno-portal website
            st.markdown("""<style>
            div.stButton > button:first-child {
            background-color: #EDBB09;
            color: rgb(51, 51, 51);
            border: 2px rgb(51, 51, 51);
            height: auto;
            width: 270px !important;
            padding-top: 10px !important
            padding-bottom: 10px !important;
            margin-left: 0%;
            } </style>""", unsafe_allow_html=True)
            if st.button("Restart Personality Quiz", type='primary'):
                st.session_state.progress = 2
                st.rerun()


    else:
        # left_co, cent_co,last_co = st.columns(3)
        # with cent_co:
        st.progress((st.session_state.progress-2)*6, text="Progress")
        # st.write(st.session_state.answers)
        st.markdown(f'''<div style="font-size:20px;"><b>{questions[st.session_state.progress]['question']}</b></div>''', unsafe_allow_html=True)
        # st.write(questions[st.session_state.progress]['question'])
        # st.image(questions[st.session_state.progress]['image'])
        show_gif(questions[st.session_state.progress]['image'])
        # st.write(questions[st.session_state.progress]['image']) # Write image name for now instead of showing image
        time.sleep(0.5)
        if st.button(questions[st.session_state.progress]['answers']['option1']['text'], type="secondary"):
            st.session_state.answers[st.session_state.progress-1] = questions[st.session_state.progress]['answers']['option1']['scores']
            st.session_state.progress = st.session_state.progress + 1
            st.rerun()
        if st.button(questions[st.session_state.progress]['answers']['option2']['text'], type="secondary"):
            st.session_state.answers[st.session_state.progress-1] = questions[st.session_state.progress]['answers']['option2']['scores']
            st.session_state.progress = st.session_state.progress + 1
            st.rerun()
        # if st.button("Previous Question", type="primary"):
        #     if st.session_state.progress > 1:
        #         st.session_state.progress = st.session_state.progress - 1
        #         st.rerun()
        #     else:
        #         st.session_state.progress = 0
        #         st.rerun()

if __name__ == "__main__":
    run()
