from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π₯ Start Generating Session π₯", callback_data="generate")],
        [InlineKeyboardButton(text="π  Return Home π ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("π₯ Start Generating Session π₯", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("π₯ Start Generating Session π₯", callback_data="generate")],
        [InlineKeyboardButton("β¨ Bot Status and More Bots β¨", url="https://t.me/StarkBots/7")],
        [
            InlineKeyboardButton("How to Use β", callback_data="help"),
            InlineKeyboardButton("πͺ About πͺ", callback_data="about")
        ],
        [InlineKeyboardButton("β₯ More Amazing bots β₯", url="https://t.me/StarkBots")],
    ]

    # Help Message
    HELP = """
"""

    # About Message
    ABOUT = """
ππππΎπππ ππ πΌπ½πππ ππ
ππΌππ : [ππππ π½ππ](t.me/skytrixszbot)
ππππ πππππππ : [πππ½π πππππ](t.me/wibuhouse)
πΌππΏ πΎππΌππππ : [πππππππππ](t.me/skytrixch)
πππππ ππππ : [πππππΌπ](t.me/skytrixsz)
    """
