# crescent-ext-kebabify

Turn your command names into kebabs.


## Installing
`pip install crescent-ext-kebabify`


## Example

```python

import crescent
from crescent.ext import kebab

bot = crescent.Bot("TOKEN")


# Make this command's name `my-class-command`
@bot.include
@kebab.ify
@crescent.command
class MyClassCommand:
    async def callback(self, ctx: crescent.Context):
        ...


# Make this command's name `my-function-command`
@bot.include
@kebab.ify
@crescent.command
async def my_function_commannd(ctx: crescent.Context):
    ...

bot.run()

```
