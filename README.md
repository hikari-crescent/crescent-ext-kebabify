# crescent-ext-kebab

Turn your command names into kebabs.

```python

import crescent
from crescent.ext import kebab

bot = crescent.Bot("TOKEN")


# Make this command's name `my-class-command`
@bot.include
@kebab.ify
@crescent.command
class MyClassCommand():
    def callback(self, ctx: crescent.Context):
        ...


# Make this command's name `my-function-command`
@bot.include
@kebab.ify
@crescent.command
def my_function_commannd(ctx: crescent.Context):
    ...

```

## Installing
requires current git version of crescent

install this library from git
