import fastf1
import pandas as pd

print("🏁 Starting F1 Pit Stop Data Test...")

# Enable cache
fastf1.Cache.enable_cache('data/cache')

try:
    print("🔄 Loading 2023 Monaco GP Qualifying session...")
    session = fastf1.get_session(2023, 'Monaco', 'Q')
    session.load()
    print("✅ Session loaded successfully!")

    # List drivers
    print("\n👨‍✈️ Drivers in session:")
    print(session.drivers)

    # Get laps for Verstappen
    laps = session.laps.pick_driver('VER')
    print("\n📊 Sample laps for VER:")
    print(laps[['LapNumber', 'LapTime', 'Compound', 'TyreLife']].head())

except Exception as e:
    print("❌ Error occurred while loading data:")
    print(e)
