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
    "errors_clear": {
        "blank": "Don't waste my time asshole.\n\nDo this: `!clear ;;` to delete all messages that match that pattern."
    },
    "errors_diary": {
      "empty": "No entries currently exist. \n\nAdd one by doing `!diary This is my first entry.`"
    },
    "error_unknown": "Can't do that... Something went wrong",
    "error_missing_permission": "Damn bro chill.\n\nYou need a permission elevation to do that.",
    "replies": {
        "joke": "Here's your shitty joke, asshole:\n\n",
        "oleg": "That's right. I fucked oleg's mom",
        "jizz": "shoombool culo",
        "sale": "Sale nègre",
        "fuckyou": "I will decimate your existence",
        "coinflip": {
            "heads": "Heads",
            "tails": "Tails"
        },
        "future": [
            "You're gonna fuck up your life.",
            "You're gonna end up being a janitor.",
            "You're gonna be a loser.",
            "You're gonna make an average living.",
            "You're gonna get rich.",
            "You're still gonna be living at your parents' house at 40.",
            "Try your luck with Twitch, cause school's not for you, buddy.",
            "You're gonna end up with a lamborghini.",
            "All you're gonna be able to afford is McDonalds.",
            "You're gonna end up a fucking peasant."
        ]
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
        "coinflip": "Flips a coin.",
        "future": "Predicts your future.",
        "diary": "Add an entry to the diary of get a random one.",
        "clear": "Clears all messages in the channel that start with a specified pattern."
    },
    "descriptions": {
        "joke": "Tells a joke based on a category. By default, category is Any.\n\n" +
                "Valid categories are: Any, Misc, Programming, Dark, Pun, Spooky, Christmas.",
        "coinflip": "Flips a coin.\n\nReplies with either 'Heads' or 'Tails'.",
        "diary": "Add an entry to the diary of get a random one.\n\n" +
                 "If no argument is provided, the reply will be a random entry.\nOtherwise, the entry will be added."
    }
}
"""
A key-value object containing the bot's replies to commands depending on the context.
"""
