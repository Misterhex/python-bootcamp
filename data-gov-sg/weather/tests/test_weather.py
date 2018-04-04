from weather import weather

def test_weather():
    w = weather("Sentosa", "deg C", 28.5, "2018-04-04T21:25:00+08:00")
    assert w.station_name ==  "Sentosa"
    reading = w.get_reading()
    assert reading == "28.5 deg C"