import inspect,os
import configs.bolt

print(inspect.getmembers(configs.bolt, inspect.isclass))