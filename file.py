from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

brands_supporting_israel = {
    # Tech Companies
    "apple": "Yes",
    "microsoft": "Yes",
    "google": "Yes",
    "intel": "Yes",
    "amazon": "Yes",
    "dell": "Yes",
    "hp": "Yes",
    "ibm": "Yes",
    "cisco": "Yes",
    "oracle": "Yes",
    "nvidia": "Yes",
    "qualcomm": "Yes",
    "tesla": "Yes",

    # Food and Beverage Companies
    "coca-cola": "Yes",
    "pepsi": "Yes",
    "starbucks": "Yes",
    "mcdonalds": "Yes",
    "burger king": "Yes",
    "kfc": "Yes",
    "subway": "Yes",
    "nestle": "Yes",
    "unilever": "Yes",
    "kellogg's": "Yes",
    "heineken": "Yes",
    "budweiser": "Yes",

    # Clothing and Fashion Brands
    "nike": "Yes",
    "adidas": "Yes",
    "puma": "Yes",
    "h&m": "Yes",
    "zara": "Yes",
    "gap": "Yes",
    "calvin klein": "Yes",
    "tommy hilfiger": "Yes",
    "ralph lauren": "Yes",
    "levis": "Yes",
    "under armour": "Yes",
    "vans": "Yes",

    # Automotive Companies
    "toyota": "Yes",
    "ford": "Yes",
    "chevrolet": "Yes",
    "bmw": "Yes",
    "mercedes-benz": "Yes",
    "volkswagen": "Yes",
    "hyundai": "Yes",
    "kia": "Yes",
    "tesla": "Yes",
    "nissan": "Yes",

    # Retail and Consumer Goods
    "walmart": "Yes",
    "target": "Yes",
    "costco": "Yes",
    "home depot": "Yes",
    "lowe's": "Yes",
    "best buy": "Yes",
    "ikea": "Yes",
    "aldi": "Yes",
    "lidl": "Yes",
    "sephora": "Yes",

    # Financial Services
    "visa": "Yes",
    "mastercard": "Yes",
    "paypal": "Yes",
    "goldman sachs": "Yes",
    "morgan stanley": "Yes",
    "bank of america": "Yes",
    "citibank": "Yes",
    "jpmorgan chase": "Yes",

    # Entertainment and Media
    "netflix": "Yes",
    "disney": "Yes",
    "warner bros": "Yes",
    "universal studios": "Yes",
    "sony pictures": "Yes",
    "spotify": "Yes",
    "hbo": "Yes",
    "hulu": "Yes",

    # Airlines and Transportation
    "delta airlines": "Yes",
    "american airlines": "Yes",
    "united airlines": "Yes",
    "emirates": "Yes",
    "qatar airways": "Yes",
    "ups": "Yes",
    "fedex": "Yes",
    "dhl": "Yes",

    # Other Domains
    "pfizer": "Yes",  # Pharmaceuticals
    "johnson & johnson": "Yes",  # Healthcare
    "3m": "Yes",  # Manufacturing
    "siemens": "Yes",  # Engineering
    "lockheed martin": "Yes",  # Defense
    "boeing": "Yes",  # Aerospace
}



async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحبا بك ,ادخل اسم المنتج او الشركة لتحقق من انها تدعم الكيان الصهيوني")


async def check_brand(update: Update, context: ContextTypes.DEFAULT_TYPE):
    brand_query = update.message.text.strip().lower()
    if brand_query in brands_supporting_israel:
        support_status = brands_supporting_israel[brand_query]
        response = f"{'يدعم ✅' if support_status == 'Yes' else 'لا يدعم ❌'}\n هذا المنتج '{brand_query.capitalize()}' {'يدعم' if support_status == 'Yes' else 'لا يدعم'} الكيان الصهيوني."
    else:
        response = f"عذرًا، ليس لدي معلومات عن المنتج '{brand_query.capitalize()}'."
    await update.message.reply_text(response)

# Main function to run the bot
def main():
   
    application = Application.builder().token("TOKER-HERE").build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, check_brand))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
