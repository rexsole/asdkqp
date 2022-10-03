from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """🇮🇹 Ciao **@{message.chat.username}** 👀
    
    🆔 {message.chat.id}
    
    📩 @ppvtbot ti permette di inviare **messaggi segreti** nei gruppi, che solo il **destinatario da te selezionato potrà visualizzare**!
    
    ⚙️ I messaggi che invierai non saranno accessibili a nessun altro.\nSolo chi lo ha scritto e il destinatario potranno visualizzarli.
    
    ❗️ Ci tengo a specificare che **il creatore del bot non ha accesso a codesti messaggi**, e **non ha** dunque **la possibilità di leggerli**.
    
    🔏 Inoltre il bot offre altre due opzioni, una per gli spoiler, ed una per mandare un messaggio che sarà leggibile da tutti tranne che da una persona, sarai tu a decidere chi.
    
    💬 **Owner: @tenente**"""

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("📝 Usami Inline!", switch_inline_query="")],
        [InlineKeyboardButton(text="🔙 Menù", callback_data="home")],
    ]
    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("📝 Usami Inline!", switch_inline_query="")
        ],
        [
            InlineKeyboardButton("🔍 Guida", callback_data="help")
        ]
    ]

    # Help Message
    HELP = "❗️ **Sintassi: @ppvtbot ciao @tenente**"

