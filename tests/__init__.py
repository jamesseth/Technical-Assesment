"""Testsuite module."""
from pathlib import Path
from sys import path as sys_path

source = str((Path(__file__).parents[1] / './src').resolve())
sys_path.append(source)
