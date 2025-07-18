import interactions as i
from utils.pallete import pal


class Ping(i.Extension):
    @i.slash_command(name="ping", description="Replies with the current ping.")
    async def ping(self, ctx: i.SlashContext):
        await ctx.defer()
        
        await ctx.send(embed=i.Embed(
            title="Ping",
            description=f"**Ping:** `{round(self.bot.latency, 2)}",
            color=i.Color.from_hex(pal.rbright())
        ))
        
        return