#!/usr/bin/python3
import os
from pathlib import Path

p = Path.cwd()
print(Path.cwd())
print(os.listdir())
print("-" * 20)
os.chdir(p.parent)

print(list(p.glob("*")))