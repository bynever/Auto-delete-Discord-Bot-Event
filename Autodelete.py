@bot.event
async def on_message(message):
  if message.channel.id == CHANNEL_ID: # ID des Channels in dem Autodeletet werden soll
    await asyncio.sleep(50) # Zeit nachdem gelöscht werden soll
    await message.delete()
  await bot.process_commands(message)