class weather:

    def __init__(self, station_name, reading_unit, reading_value, timestamp):
        self.station_name = station_name
        self.reading_unit = reading_unit 
        self.reading_value = reading_value
        self.timestamp = timestamp 
    
    def get_reading(self):
        return "{} {}".format(self.reading_value, self.reading_unit)

    def __str__(self):
        return "Station: {} , Reading: {} @ {}".format(self.station_name, self.get_reading(),self.timestamp)