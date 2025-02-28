import sqlite3

CONN = sqlite3.connect('car_brands.db')
CURSOR = CONN.cursor()
