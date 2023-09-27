# OpenCage Geocoding API configuration
api_key_opencage = "your-api-key-here"  # INSERT YOUR API KEY HERE
base_url_opencage = "https://api.opencagedata.com/geocode/v1/json"

# Mapbox access token for visualizations
mapbox_access_token = "your-api-key-here"  # INSERT YOUR API KEY HERE

# Define the boundaries of Europe (latitude and longitude)
min_lat = 36.0  # Southernmost point
max_lat = 71.0  # Northernmost point
min_lon = -11.0  # Westernmost point
max_lon = 40.0  # Easternmost point

# Define the grid spacing
grid_spacing = 1  # 1 degree latitude/longitude equals 10000 kilometers or so

# OpenRouteService API key and base URL
api_key_openrouteservice = "your-api-key-here"  # INSERT YOUR API KEY HERE
base_url_openrouteservice = "https://api.openrouteservice.org/v2/matrix/driving-hgv"  # hgv = heavy goods vehicle

# driving cost per tonne-km
drivingcost_per_tonnekm = 0.15  # euro per tonne-km (example, replace with real value)

# Facility tonnes per year processed EOL LIBs [cell weight equivalents]
Facility = 98667
