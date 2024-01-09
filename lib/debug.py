#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.family import Family
from models.job import Job
from models.sitter import Sitter
import ipdb


family = Family('wise', 2, 13905)
sitter = Sitter('Erin', 13905, 25)



ipdb.set_trace()
