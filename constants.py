### INLCUDE
"""
For generating the Facility grid
"""
# OpenCage Geocoding API configuration
api_key_opencage = "your_opencage_api"
base_url_opencage = "https://api.opencagedata.com/geocode/v1/json"

# Define the boundaries of Europe (latitude and longitude)
min_lat = 36.0  # Southernmost point
max_lat = 71.0  # Northernmost point
min_lon = -11.0  # Westernmost point
max_lon = 40.0  # Easternmost point

# Define the grid spacing (10000 kilometers or so)
grid_spacing = 1  # About 1 degree latitude/longitude

### EXCLUDE


### CODE

# OpenRouteService API key and base URL
api_key_openrouteservice = "your_openrouteservice_api"
base_url_openrouteservice = "https://api.openrouteservice.org/v2/matrix/driving-hgv"  # hgv = heavy goods vehicle

# Mapbox access token
mapbox_access_token = "your_mapbox_api"

# Facility tonnes per year processed EOL LIBs [cell weight equivalents]
Facility = 98667

# Pack share volumes per year from CES POM and AfR (Jan'22) categories:
# Personal Mobility, Light EV, Heavy EV, Industrial, ESS, Maritime
pack_share_POM_2022 = 0.893
pack_share_POM_2026 = 0.931
pack_share_POM_2030 = 0.964
pack_share_AfR_2022 = 0.214
pack_share_AfR_2026 = 0.343
pack_share_AfR_2030 = 0.538

# Volumes per year in [tonnes] from CES AfR(Jan'22), total of all categories
AfR_total_2022 = 38003
AfR_total_2026 = 63337
AfR_total_2030 = 121884

# Average weight share of battery module compared to pack weight for EV batteries
# with cathode chemistries: LFP, LMO, NCA, NMC111, NMC622, and NMC811
pack_to_cell_ratio_average = 0.723

# Percentage of LIB scrap from cell producers of batteries placed on the market
LIB_scrap_percentage_POM = 0.10

"""
For calculating transport costs and co2 emissions
"""

# driving cost per tonne-km (LOW VALUE)
drivingcost_per_tonnekm_LOW = (
    1.36 / 21
)  # ref Barcelone 7/6 https://della.eu/price/local/

# driving cost per tonne-km (HIGH VALUE)
# Assume linearly increasing cost which is equivalent to 40% of the average of the
# OPEX & CAPEX price of all technologies for the facility for a total S2F2D distance
# of 2000km or about the distance from Madrid to Berlin
AverageFixedPrice = 1522348259
drivingcost_per_tonnekm_HIGH = AverageFixedPrice / 2000 / Facility

# calculate tonnes CO2 per ton
tonCO2_per_tonnekm = (
    55 / 1000000
)  # tonne CO2 per tonne-km, ref https://www.transportenvironment.org/wp-content/uploads/2021/10/202108_truck_CO2_report_final.pdf
