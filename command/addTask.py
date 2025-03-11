import discord
from datetime import datetime
import command.db
from command.model.Task import Task

async def addTask(ctx, task_info: str):
    try:
        memberid = ctx.author.id
        username = ctx.author.name
        avatar = ctx.author.avatar

        # Kiểm tra định dạng input
        task_info = task_info.split(' - ')
        if len(task_info) != 3:
            raise ValueError("Invalid input format. Expected format: name - description - time")

        name, description, time = task_info

        # Tạo đối tượng Task
        task = Task(memberid,name, description, time, "False")

        try:
            command.db.add_task(task)
        except Exception as db_error:
            await ctx.send(f"❌ Database error: {db_error}")
            return

        # Tạo embed thông báo thành công
        embed = discord.Embed(
            title="✅ Task Added Successfully!",
            description=f"```{task.__str__()}```",
            colour=0xd4add7,
            timestamp=datetime.now()
        )

        embed.set_author(name=username)
        embed.set_thumbnail(url=avatar)
        embed.set_footer(icon_url="https://i.imgur.com/fumd8iG.jpeg")

        await ctx.send(embed=embed)

    except ValueError as ve:
        await ctx.send(f"❌ Input error: {ve}")

    except Exception as e:
        await ctx.send(f"❌ Unexpected error: {e}")
