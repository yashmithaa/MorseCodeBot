import hikari
import lightbulb

bot = lightbulb.BotApp(
    token='OTkyMDAzNzMyODMxMjI3OTI0.G51jXF.bLrW-mRHkBLOXG8f1YIa0g65nPIVVrBQ75MTB8',
    prefix = 'boi ', 
    default_enabled_guilds=(762287566690844692)
)

@bot.listen(hikari.StartedEvent)
async def onstart(event):
    print("Bot is now online")

morse_code ={'A':'.-', 'B':'-...', 'C': '-.-.', 'D': '-..',
                'E' : '.', 'F':'..-.', 'G':'--.','H':'....','I':'..',
                'J':'.---','K':"-.-", 'L':".-..", 'M':'--', "N":'-.',
                'O' : '---','P': '.--.', 'Q':'--.-','R':'.-.','S':'...',
                'T':'-','U':'..-','V':'...-','W':'.--','X':'-..-','Y':'-.--','Z':'--..'}


@bot.command
@lightbulb.command('hello','Clare wants to say hello')
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx):    
    await ctx.respond("hello I'm Clare.Nice to meet you")

@bot.command
@lightbulb.option('letter','Enter a letter')
@lightbulb.command('teach','Clare wants to teach you Morse code!')
@lightbulb.implements(lightbulb.SlashCommand)
async def ping(ctx):
    choice = ctx.options.letter.upper()
    await ctx.respond(morse_code[choice])

@bot.command
@lightbulb.command('revise','Makes you revise morse-code from A-Z')
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx):
    for letter in morse_code:
        this = letter + ' : '+ morse_code[letter]
        await ctx.respond(this)

@bot.command
@lightbulb.option('text','Enter the text you wanna translate',modifier=lightbulb.OptionModifier.GREEDY)
@lightbulb.command('morse','Translates text to morse code')
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx):
    translated=''
    
    listToStr = ' '.join([str(elem) for elem in ctx.options.text])
    sentence = listToStr.upper()
    for letter in sentence:
        if letter==' ':
            translated = translated + ' / '
        else:
            translated = translated + ' ' + morse_code[letter] + ' '
    await ctx.respond(translated)

def get_key(val):
    for key, value in morse_code.items():
        if val == value:
            return key

@bot.command
@lightbulb.option('morse','Enter the code you wanna translate',modifier=lightbulb.OptionModifier.GREEDY)
@lightbulb.command('text','Translates text to morse code')
@lightbulb.implements(lightbulb.PrefixCommand)
async def ping(ctx):
    translated=''
    
    code = ctx.options.morse
    
    for i in code:
        if i=='/':
            translated = translated + ' '
        if i in morse_code.values():
            key = get_key(i)
            translated = translated  + key 
        '''else:
            translated = translated + ' error '''
    await ctx.respond(translated.lower())
bot.run()