# About The Project

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/erikemilsson/ELiMINATE_EU_MFA">
    <img src="example_images/Eliminate_logo.png" alt="Logo">
  </a>

<h3 align="center">A Supplier-Facility-Customer facility optimization problem with linear programming.</h3>

</div>

<!-- ABOUT THE PROJECT -->
The code in this repository is based on the EU project <a href="https://www.vinnova.se/en/p/end-of-life-li-ion-battery-management-integration-and-technology-evaluation-eliminate/">ELiMINATE</a> (End-of-Life Li-ion Battery Management Integration and Technology Evaluation), in which a reverse-logistics network optimization was solved for the lithium-ion battery supply chain. 

The Supply and Demand Excel files were represented by the collectors and producers data (respectively):
<a href="https://chart-studio.plotly.com/~erikemilsson/23/#/">
  <img src="https://github.com/erikemilsson/ELiMINATE_EU_MFA/blob/main/example_images/Collectors_Year_2030.png" width="400" height="300" alt="Collectors">
</a>

<a href="https://chart-studio.plotly.com/~erikemilsson/5">
  <img src="https://github.com/erikemilsson/ELiMINATE_EU_MFA/blob/main/example_images/Producers_Year_2030.png" width="400" height="300" alt="Producers">
</a>

The results of the optimization were presented with maps, like here:

<a href="https://github.com/erikemilsson/ELiMINATE_EU_MFA/blob/main/example_images/optimization_novel1current1current2_CO2_2030.png">
  <img src="https://github.com/erikemilsson/ELiMINATE_EU_MFA/blob/main/example_images/optimization_novel1current1current2_CO2_2030.png" width="400" height="300" alt="Optimization">
</a>

To see more about the project, please refer to the [report](https://ivl.diva-portal.org/smash/get/diva2:1822105/FULLTEXT01.pdf).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With

* <a href="https://pypi.org/project/PuLP">PuLP 2.7.0</a>
* <a href="https://opencagedata.com">OpenCage Geocoding API</a>
* <a href="https://plotly.com">plotly</a>
* <a href="https://mapbox.com">mapbox</a>

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

The repository and the sample data is currently applied to a forecast of the European battery market for 2030.
This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Installation

1. Get free APIs keys at
    - [mapbox](https://mapbox.com)
    - [OpenCage Geocoding API](https://opencagedata.com)
    - [openroute service](https://openrouteservice.org)
  
2. Clone the repo
   ```sh
   git clone https://github.com/erikemilsson/ELiMINATE_EU_MFA
   ```

3. Create a `.env` file in the project root and add your API keys:
   ```sh
   cp .env.example .env
   ```
   Then edit `.env` and add your actual API keys:
   ```
   OPENCAGE_API_KEY=your-opencage-api-key-here
   MAPBOX_ACCESS_TOKEN=your-mapbox-token-here
   OPENROUTESERVICE_API_KEY=your-openrouteservice-key-here
   ```
   
4. Enter your data to
   - Demand.xlsx
   - Facilities.xlsx
   - Supply.xlsx
   - constantsfile.py

### Running Optimization

1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. Run `Preparation (run before optimization).ipynb` one time to generate the preprocessed data

3. Open `Optimization.ipynb` and set the number of facilities to optimize for:
   ```py
   number_of_facilities = 3  # Example: optimize for 3 facilities
   ```

4. Run `Optimization.ipynb` to solve the optimization problem and visualize results


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<!--
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>
-->

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Erik Emilsson - [www.erikemilsson.com](https://www.erikemilsson.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
