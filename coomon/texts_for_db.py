from aiogram.utils.formatting import Bold, as_list, as_marked_section


categories = ['Products', 'Drinks']

description_for_info_pages = {
    "main": "Welcome!",
    "about": "Our restaurent.\nThe working mode is 24/7.",
    "payment": as_marked_section(
        Bold("Payment options:"),
        "With a card in the bot",
        "On receipt of the card/cache",
        "In restaurent",
        marker="✅ ",
    ).as_html(),
    "shipping": as_list(
        as_marked_section(
            Bold("shipping options:"),
            "Courier",
            "Self-delivery (I'll be right there to pick it up).",
            "I'll eat at your place (I'll be right there).",
            marker="✅ ",
        ),
        as_marked_section(Bold("You can't:"), "Post office", "Birds", marker="❌ "),
        sep="\n----------------------\n",
    ).as_html(),
    'catalog': 'Categories:',
    'cart': 'There is nothing in the cart!'
}