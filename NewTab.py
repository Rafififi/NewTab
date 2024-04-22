import os
import sqlite3


def find_path():
    profiles_path = os.path.expanduser("~/.mozilla/firefox/")
    profiles = [profile for profile in os.listdir(profiles_path) if '.default' in profile]
    selected_profile = None
    for profile in profiles:
        if os.path.isfile(os.path.join(profiles_path, profile, 'places.sqlite')):
            selected_profile = profile
            break
    return '/home/rafael/.mozilla/firefox/' + selected_profile + '/places.sqlite'


conn = sqlite3.connect(find_path())

cur = conn.cursor()

cur.execute("SELECT url FROM moz_places ORDER BY visit_count DESC LIMIT 36")

rows = cur.fetchall()

for row in rows:
    print(row[0])

conn.close()
