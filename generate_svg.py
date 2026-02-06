import datetime

with open("profile.svg", "w") as f:
    f.write(f"""<svg width="200" height="60" xmlns="http://www.w3.org/2000/svg">
  <text x="10" y="35" font-size="24">Profile updated: {datetime.datetime.now().strftime('%Y-%m-%d')}</text>
</svg>
""")