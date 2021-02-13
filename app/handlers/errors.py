from loguru import logger
from app import dp, config


@dp.errors_handler()
async def errors_handler(update, exception):
    """Exceptions handler. Catches all
    exceptions within task factory tasks."""
    
    message = f"Error:\n{exception}\n\nUpdate: {update}"

    # Iterate through superusers and try to send an error message
    for superuser in config.superusers:
        if not superuser:
            continue

        try:
            await dp.bot.send_message(superuser, message)
        except:
            continue
        
    logger.exception(message)
