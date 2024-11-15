from flask import Flask, flash


import sqlite3

app = Flask(__name__)

from app import routes