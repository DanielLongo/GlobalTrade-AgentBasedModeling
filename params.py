from country import NationAgent 

country_names = ["USA", "China", "Russia", "UK", "India", "France", "Germany", "Vietnam", "Brazil", "Iran", "North Korea"]

### COUNTRY RELATIONS ###

# less contested
trade_relations_less_contested = [
    {"country_names": {"USA", "Canada"}, "friendliness": 0.95},
    {"country_names": {"USA", "China"}, "friendliness": 0.5},
    {"country_names": {"USA", "Russia"}, "friendliness": 0.2},
    {"country_names": {"USA", "UK"}, "friendliness": 0.9},
    {"country_names": {"USA", "India"}, "friendliness": 0.8},
    {"country_names": {"USA", "France"}, "friendliness": 0.85},
    {"country_names": {"USA", "Germany"}, "friendliness": 0.85},
    {"country_names": {"USA", "Vietnam"}, "friendliness": 0.6},
    {"country_names": {"USA", "Brazil"}, "friendliness": 0.75},
    {"country_names": {"USA", "Iran"}, "friendliness": 0.1},
    {"country_names": {"USA", "North Korea"}, "friendliness": 0.1},
    {"country_names": {"China", "Russia"}, "friendliness": 0.5},
    {"country_names": {"China", "UK"}, "friendliness": 0.5},
    {"country_names": {"China", "India"}, "friendliness": 0.6},
    {"country_names": {"China", "France"}, "friendliness": 0.6},
    {"country_names": {"China", "Germany"}, "friendliness": 0.6},
    {"country_names": {"China", "Vietnam"}, "friendliness": 0.9},
    {"country_names": {"China", "Brazil"}, "friendliness": 0.7},
    {"country_names": {"China", "Iran"}, "friendliness": 0.4},
    {"country_names": {"China", "North Korea"}, "friendliness": 0.8},
    {"country_names": {"Russia", "UK"}, "friendliness": 0.6},
    {"country_names": {"Russia", "India"}, "friendliness": 0.7},
    {"country_names": {"Russia", "France"}, "friendliness": 0.6},
    {"country_names": {"Russia", "Germany"}, "friendliness": 0.6},
    {"country_names": {"Russia", "Vietnam"}, "friendliness": 0.8},
    {"country_names": {"Russia", "Brazil"}, "friendliness": 0.7},
    {"country_names": {"Russia", "Iran"}, "friendliness": 0.7},
    {"country_names": {"Russia", "North Korea"}, "friendliness": 0.9},
    {"country_names": {"UK", "India"}, "friendliness": 0.8},
    {"country_names": {"UK", "France"}, "friendliness": 0.9},
    {"country_names": {"UK", "Germany"}, "friendliness": 0.9},
    {"country_names": {"UK", "Vietnam"}, "friendliness": 0.6},
    {"country_names": {"UK", "Brazil"}, "friendliness": 0.7},
    {"country_names": {"UK", "Iran"}, "friendliness": 0.2},
    {"country_names": {"UK", "North Korea"}, "friendliness": 0.2},
    {"country_names": {"India", "France"}, "friendliness": 0.8},
    {"country_names": {"India", "Germany"}, "friendliness": 0.8},
    {"country_names": {"India", "Vietnam"}, "friendliness": 0.7},
    {"country_names": {"India", "Brazil"}, "friendliness": 0.8},
    {"country_names": {"India", "Iran"}, "friendliness": 0.5},
    {"country_names": {"India", "North Korea"}, "friendliness": 0.5},
    {"country_names": {"France", "Germany"}, "friendliness": 0.9},
    {"country_names": {"France", "Vietnam"}, "friendliness": 0.6},
    {"country_names": {"France", "Brazil"}, "friendliness": 0.7},
    {"country_names": {"France", "Iran"}, "friendliness": 0.2},
    {"country_names": {"France", "North Korea"}, "friendliness": 0.2},
    {"country_names": {"Germany", "Vietnam"}, "friendliness": 0.6},
    {"country_names": {"Germany", "Brazil"}, "friendliness": 0.7},
    {"country_names": {"Germany", "Iran"}, "friendliness": 0.2},
    {"country_names": {"Germany", "North Korea"}, "friendliness": 0.2},
    {"country_names": {"Vietnam", "Brazil"}, "friendliness": 0.8},
    {"country_names": {"Vietnam", "Iran"}, "friendliness": 0.5},
    {"country_names": {"Vietnam", "North Korea"}, "friendliness": 0.5},
    {"country_names": {"Brazil", "Iran"}, "friendliness": 0.5},
    {"country_names": {"Brazil", "North Korea"}, "friendliness": 0.5},
    {"country_names": {"Iran", "North Korea"}, "friendliness": 0.1}
]
     
# more contested
# squared friendliness of less contest countries plus a little
trade_relations_more_contested = trade_relations_less_contested[::]
for trade_relation in trade_relations_more_contested:
    trade_relation["friendliness"] = (max(trade_relation["friendliness"] + .1, 1)) **2 +.5



### COUNTRIES ###
# India
india_population_params = {
        "population": 1366417756,
        "population_growth_rate": 1.015,
        "population_growth_acceleration": 0.0005
    }

india_gdp = {
    "gdp": 2.87 * 10**12,
    "gdp_growth_rate": 1.03,
    "gdp_growth_acceleration": 0.0001
}

india_human_development_params = {
    "human_development_index": 0.645,
    "human_development_rate": 1.008,
    "human_development_acceleration": 0.00005
}

INDIA = NationAgent(name="India", gdp=india_gdp, natural_resources=0.5, imports=800, export=500, population_params=india_population_params, human_development_params=india_human_development_params)


# France
france_population_params = {
        "population": 67418687,
        "population_growth_rate": 1.003,
        "population_growth_acceleration": 0.0002
    }

france_gdp = {
    "gdp": 2.84 * 10**12,
    "gdp_growth_rate": 1.015,
    "gdp_growth_acceleration": 0.0001
}

france_human_development_params = {
    "human_development_index": 0.901,
    "human_development_rate": 1.003,
    "human_development_acceleration": 0.00005
}

FRANCE = NationAgent(name="France", gdp=france_gdp, natural_resources=0.2, imports=600, export=550, population_params=france_population_params, human_development_params=france_human_development_params)


# Germany
germany_population_params = {
        "population": 83783942,
        "population_growth_rate": 1.002,
        "population_growth_acceleration": 0.0001
    }

germany_gdp = {
    "gdp": 4.17 * 10**12,
    "gdp_growth_rate": 1.017,
    "gdp_growth_acceleration": 0.0001
}

germany_human_development_params = {
    "human_development_index": 0.939,
    "human_development_rate": 1.004,
    "human_development_acceleration": 0.00005
}

GERMANY = NationAgent(name="Germany", gdp=germany_gdp, natural_resources=0.3, imports=700, export=600, population_params=germany_population_params, human_development_params=germany_human_development_params)


# Vietnam
vietnam_population_params = {
        "population": 97429061,
        "population_growth_rate": 1.022,
        "population_growth_acceleration": 0.0005
    }

vietnam_gdp = {
    "gdp": 0.3 * 10**12,
    "gdp_growth_rate": 1.05,
    "gdp_growth_acceleration": 0.0001
}

vietnam_human_development_params = {
    "human_development_index": 0.694,
    "human_development_rate": 1.012,
    "human_development_acceleration": 0.00005
}

VIETNAM = NationAgent(name="Vietnam", gdp=vietnam_gdp, natural_resources=0.6, imports=300, export=200, population_params=vietnam_population_params, human_development_params=vietnam_human_development_params)


usa_population_params = {
    "population": 328915700,
    "population_growth_rate": 1.007,
    "population_growth_acceleration": 0.0001
}

usa_gdp = {
    "gdp": 21.44 * 10**12,
    "gdp_growth_rate": 1.02,
    "gdp_growth_acceleration": 0.0001
}

usa_human_development_params = {
    "human_development_index": 0.926,
    "human_development_rate": 1.004,
    "human_development_acceleration": 0.00005
}

USA = NationAgent(name="USA", gdp=usa_gdp, natural_resources=.7, imports=1000, export=700, population_params=usa_population_params, human_development_params=usa_human_development_params)


china_population_params = {
    "population": 1392730000,
    "population_growth_rate": 1.004,
    "population_growth_acceleration": 0.0001
}

china_gdp = {
    "gdp": 14.14 * 10**12,
    "gdp_growth_rate": 1.06,
    "gdp_growth_acceleration": 0.0002
}

china_human_development_params = {
    "human_development_index": 0.752,
    "human_development_rate": 1.007,
    "human_development_acceleration": 0.0001
}

CHINA = NationAgent(name="China", gdp=china_gdp, natural_resources=.5, imports=1200, export=2200, population_params=china_population_params, human_development_params=china_human_development_params)


russia_population_params = {
    "population": 144498200,
    "population_growth_rate": 1.001,
    "population_growth_acceleration": 0.0001
}

russia_gdp = {
    "gdp": 1.64 * 10**12,
    "gdp_growth_rate": 1.03,
    "gdp_growth_acceleration": 0.0001
}

russia_human_development_params = {
    "human_development_index": 0.824,
    "human_development_rate": 1.002,
    "human_development_acceleration": 0.00005
}

RUSSIA = NationAgent(name="Russia", gdp=russia_gdp, natural_resources=.8, imports=600, export=800, population_params=russia_population_params, human_development_params=russia_human_development_params)


uk_population_params = {
    "population": 67600000,
    "population_growth_rate": 1.002,
    "population_growth_acceleration": 0.0001
}

uk_gdp = {
    "gdp": 2.62 * 10**12,
    "gdp_growth_rate": 1.02,
    "gdp_growth_acceleration": 0.0001
}

uk_human_development_params = {
    "human_development_index": 0.932,
    "human_development_rate": 1.002,
    "human_development_acceleration": 0.00005
}

UK = NationAgent(name="UK", gdp=uk_gdp, natural_resources=.3, imports=800, export=1000, population_params=uk_population_params, human_development_params=uk_human_development_params)

# Agent for Canada
canada_population_params = {
        "population": 37995000,
        "population_growth_rate": 1.005,
        "population_growth_acceleration": 0.0005
    }

canada_gdp = {
    "gdp": 1.84 * 10**12,
    "gdp_growth_rate": 1.03,
    "gdp_growth_acceleration": 0.0002
}

canada_human_development_params = {
    "human_development_index": 0.929,
    "human_development_rate": 1.005,
    "human_development_acceleration": 0.0001
}

CANADA = NationAgent(name="Canada", gdp=canada_gdp, natural_resources=.55, imports=500, export=400, population_params=canada_population_params, human_development_params=canada_human_development_params)


# Agent for Australia
australia_population_params = {
        "population": 25687000,
        "population_growth_rate": 1.01,
        "population_growth_acceleration": 0.0005
    }

australia_gdp = {
    "gdp": 1.48 * 10**12,
    "gdp_growth_rate": 1.03,
    "gdp_growth_acceleration": 0.0002
}

australia_human_development_params = {
    "human_development_index": 0.944,
    "human_development_rate": 1.005,
    "human_development_acceleration": 0.0001
}

AUSTRALIA = NationAgent(name="Australia", gdp=australia_gdp, natural_resources=.4, imports=300, export=250, population_params=australia_population_params, human_development_params=australia_human_development_params)


# Agent for Mexico
mexico_population_params = {
        "population": 132328000,
        "population_growth_rate": 1.015,
        "population_growth_acceleration": 0.0007
    }

mexico_gdp = {
    "gdp": 1.28 * 10**12,
    "gdp_growth_rate": 1.02,
    "gdp_growth_acceleration": 0.0003
}

mexico_human_development_params = {
    "human_development_index": 0.774,
    "human_development_rate": 1.005,
    "human_development_acceleration": 0.0001
}

MEXICO = NationAgent(name="Mexico", gdp=mexico_gdp, natural_resources=.2, imports=200, export=250, population_params=mexico_population_params, human_development_params=mexico_human_development_params)


# Agent for Nigeria
nigeria_population_params = {
        "population": 211401000,
        "population_growth_rate": 1.025,
        "population_growth_acceleration": 0.001
    }

nigeria_gdp = {
    "gdp": 448.12 * 10**9,
    "gdp_growth_rate": 1.045,
    "gdp_growth_acceleration": 0.0004
}

nigeria_human_development_params = {
    "human_development_index": 0.542,
    "human_development_rate": 1.005,
    "human_development_acceleration": 0.0001
}

NIGERIA = NationAgent(name="Nigeria", gdp=nigeria_gdp, natural_resources=.3, imports=100, export=150, population_params=nigeria_population_params, human_development_params=nigeria_human_development_params)

# Iran
iran_population_params = {
    "population": 84747_000,
    "population_growth_rate": 1.015,
    "population_growth_acceleration": 0.001
}

iran_gdp = {
    "gdp": 454.13 * 10**9,
    "gdp_growth_rate": 1.01,
    "gdp_growth_acceleration": 0.0001
}

iran_human_development_params = {
    "human_development_index": 0.783,
    "human_development_rate": 1.005,
    "human_development_acceleration": 0.00005
}

IRAN = NationAgent(name="Iran", gdp=iran_gdp, natural_resources=0.25, imports=50, export=40, 
                   population_params=iran_population_params, human_development_params=iran_human_development_params)

# North Korea
nk_population_params = {
    "population": 25779_450,
    "population_growth_rate": 1.01,
    "population_growth_acceleration": 0.0005
}

nk_gdp = {
    "gdp": 17.4 * 10**9,
    "gdp_growth_rate": 1.03,
    "gdp_growth_acceleration": 0.00005
}

nk_human_development_params = {
    "human_development_index": 0.75,
    "human_development_rate": 1.001,
    "human_development_acceleration": 0.0001
}

NORTH_KOREA = NationAgent(name="North Korea", gdp=nk_gdp, natural_resources=0.2, imports=80, export=10, 
                          population_params=nk_population_params, human_development_params=nk_human_development_params)

# Brazil
brazil_population_params = {
    "population": 214469381,
    "population_growth_rate": 1.007,
    "population_growth_acceleration": 0.0001
}

brazil_gdp = {
    "gdp": 2.05 * 10**12,
    "gdp_growth_rate": 1.01,
    "gdp_growth_acceleration": 0.0001
}

brazil_human_development_params = {
    "human_development_index": 0.765,
    "human_development_rate": 1.003,
    "human_development_acceleration": 0.00005
}

BRAZIL = NationAgent(
    name="Brazil",
    gdp=brazil_gdp,
    natural_resources=0.85,
    imports=1000,
    export=800,
    population_params=brazil_population_params,
    human_development_params=brazil_human_development_params
)



all_countries = [INDIA, CHINA, USA, RUSSIA, GERMANY, FRANCE, UK, CANADA, AUSTRALIA, MEXICO, NIGERIA, IRAN, NORTH_KOREA, VIETNAM, BRAZIL]