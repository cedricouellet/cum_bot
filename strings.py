"""
Contains a key-value object containing the bot's replies to commands depending on the context.
"""

strings = {
    "errors_math": {
        "overflow": "Jesus christ man, do you think I'm a calculator?",
        "invalid": "What the fuck is that.Seriously, I'm not even joking.\n\nAre you brain dead?",
        "blank": "Don't waste my time asshole.\n\n Do this `!math 1+1`, dumbass nigga."
    },
    "errors_joke": {
        "http_error": "Fuck my internet's down.\n\nTry again later.",
        "invalid": "That's not a valid joke category, you dumb fuck.\n\n" +
                   "The valid categories are: *Any, Misc, Programming, Dark, Pun, Spooky, Christmas*"
    },
    "errors_gif": {
        "http_error": "Fuck my internet's down.\n\nTry again later.",
        "unexpected": "Could't fetch a GIF for that.\n\nTry again with a different search."
    },
    "errors_weather": {
        "http_error": "Fuck my internet's down.\n\nTry again later.",
        "invalid": "That's not a valid city, you dumb fuck.\n\nTry something else.",
        "blank": "Don't waste my time asshole, you've gotta give me a city.\n\nTry `!weather Toronto`, retard"
    },
    "error_unknown": "Can't do that... Something went wrong",
    "replies": {
        "joke": "Here's your shitty joke, asshole:\n\n",
        "oleg": "That's right. I fucked oleg's mom",
        "jizz": "shoombool culo",
        "sale": "Sale nègre",
        "fuckyou": "I will decimate your existence",
        "coinflip": {
            "heads": "Heads",
            "tails": "Tails"
        }
    },
    "tags": {
        "cedric": "<@359068019286212618>",
        "eli": "<@337754436304896000>",
        "felix": "<@181490764734398464>"
    },
    "briefs": {
        "help": "Shows this message.",
        "code": "Display the bot's code.",
        "sale": "REDACTED.",
        "jizz": "REDACTED.",
        "fuckyou": "REDACTED.",
        "oleg": "REDACTED.",
        "jew": "Summon Eli.",
        "crackhead": "Summon Felix.",
        "loser": "Summon Cedric.",
        "math": "Calculate a math expression.",
        "joke": "Tells a joke based on a category. By default, category is Any.",
        "gif": "Searches a GIF by its name or gets a trending gif.",
        "weather": "Gets the weather for a specific city.",
        "coinflip": "Flips a coin."
    },
    "descriptions": {
        "joke": "Valid categories are: Any, Misc, Programming, Dark, Pun, Spooky, Christmas.",
        "coinflip": "Flips a coin.\n\nReplies with either 'Heads' or 'Tails'."
    }
}
"""
A key-value object containing the bot's replies to commands depending on the context.
"""