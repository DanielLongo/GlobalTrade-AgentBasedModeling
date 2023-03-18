
import math
class NationAgent():
    def __init__(self, name, gdp, natural_resources, imports, export, population_params, human_development_params):
        self.name = name
        self.gdp = gdp
        self.natural_resources = natural_resources
        self.imports = imports
        self.export = export
        self.population = population_params
        self.human_development = human_development_params

    def get_json(self):
        return {
            "name": self.name,
            "gdp": self.gdp["gdp"],
            "natural_resources": self.natural_resources,
            "imports": self.imports,
            "exports": self.export,
            "population": self.population["population"],
            "human_development": self.human_development["human_development_index"],
            "gdp_per_capita": self.get_gdp_per_capita(),
        }
    
    def get_gdp_per_capita(self):
        return self.gdp["gdp"] / self.population["population"]
    
    def step(self):
        # both human population params and human development params are dictionaries contain 1st and 2nd order derivatives
        population_growth_rate = self.population["population_growth_rate"] +  ((self.population["population_growth_acceleration"]) ** 2 )/2
        self.population["population"] *= population_growth_rate
        self.population["population_growth_rate"] = population_growth_rate

        human_development_rate = self.human_development["human_development_rate"] +  ((self.human_development["human_development_acceleration"]) ** 2 )/2
        new_human_development_index = min(1, self.human_development["human_development_index"] * human_development_rate)
        self.human_development["human_development_index"] = new_human_development_index
        self.human_development["human_development_rate"] = human_development_rate

        gdp_growth_rate = self.gdp["gdp_growth_rate"] +  ((self.gdp["gdp_growth_acceleration"]) ** 2 )/2
        self.gdp["gdp"] *= gdp_growth_rate
        self.gdp["gdp_growth_rate"] = gdp_growth_rate


usa_population_params = {
        "population": 248709873,
        "population_growth_rate": 1.01,
        "population_growth_acceleration": 0.001
    }

usa_gdp = {
    "gdp": 5.97 * 10**12,
    "gdp_growth_rate": 1.02,
    "gdp_growth_acceleration": 0.0001
}

usa_human_development_params = {
    "human_development_index": 0.865,
    "human_development_rate": 1.005,
    "human_development_acceleration": 0.00005
}


USA = NationAgent(name="USA", gdp=usa_gdp, natural_resources=.7, imports=1000, export=700, population_params=usa_population_params, human_development_params=usa_human_development_params)


china_population_params = {
    "population": 1.135 * 10**9,
    "population_growth_rate": 1.04,
    "population_growth_acceleration": 0.002
}

china_gdp = {
    "gdp": 3.93 * 10**12,
    "gdp_growth_rate": 1.07,
    "gdp_growth_acceleration": 0.0002
}

china_human_development_params = {
    "human_development_index": 0.758,
    "human_development_rate": 1.01,
    "human_development_acceleration": 0.0001
}

CHINA = NationAgent(name="China", gdp=china_gdp, natural_resources=.7, imports=1000, export=700, population_params=china_population_params, human_development_params=china_human_development_params)


russia_population_params = {
    "population": 14816458,
    "population_growth_rate": 0.99,
    "population_growth_acceleration": -0.001
}

russia_gdp = {
    "gdp": 0.514 * 10**12,
    "gdp_growth_rate": 0.98,
    "gdp_growth_acceleration": -0.0001
}

russia_human_development_params = {
    "human_development_index": 0.816,
    "human_development_rate": 0.995,
    "human_development_acceleration": -0.00005
}

RUSSIA = NationAgent(name="Russia", gdp=russia_gdp, natural_resources=.7, imports=1000, export=700, population_params=russia_population_params, human_development_params=russia_human_development_params)

# usa_population_params = {
#         "population": 248709873,
#         "population_growth_rate": 1.01,
#         "population_growth_acceleration": 0.001
#     }

# usa_gdp = {
#     "gdp": 5.97 * 10**12,
#     "gdp_growth_rate": 1.02,
#     "gdp_growth_acceleration": 0.0001
# }

# usa_human_development_params = {
#     "human_development_index": 0.865,
#     "human_development_rate": 1.005,
#     "human_development_acceleration": 0.00005
# }


# USA = NationAgent(name="USA", gdp=usa_gdp, natural_resources=.7, imports=1000, export=700, population_params=usa_population_params, human_development_params=usa_human_development_params)


# china_population_params = {
#     "population": 1.135 * 10**9,
#     "population_growth_rate": 1.04,
#     "population_growth_acceleration": 0.002
# }

# china_gdp = {
#     "gdp": 3.93 * 10**12,
#     "gdp_growth_rate": 1.07,
#     "gdp_growth_acceleration": 0.0002
# }

# china_human_development_params = {
#     "human_development_index": 0.758,
#     "human_development_rate": 1.01,
#     "human_development_acceleration": 0.0001
# }

# CHINA = NationAgent(name="China", gdp=china_gdp, natural_resources=.7, imports=1000, export=700, population_params=china_population_params, human_development_params=china_human_development_params)


# russia_population_params = {
#     "population": 14816458,
#     "population_growth_rate": 0.99,
#     "population_growth_acceleration": -0.001
# }

# russia_gdp = {
#     "gdp": 0.514 * 10**12,
#     "gdp_growth_rate": 0.98,
#     "gdp_growth_acceleration": -0.0001
# }

# russia_human_development_params = {
#     "human_development_index": 0.816,
#     "human_development_rate": 0.995,
#     "human_development_acceleration": -0.00005
# }

# RUSSIA = NationAgent(name="Russia", gdp=russia_gdp, natural_resources=.7, imports=1000, export=700, population_params=russia_population_params, human_development_params=russia_human_development_params)
if __name__ == "__main__":
    # Define starting values for 1990
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

    logs = []
    import matplotlib.pyplot as plt
    import numpy as np
    for i in range(30):
        USA.step()
        logs.append(USA.get_json())

    # graph key variables

    # population
    plt.plot(np.array([x["population"] for x in logs]))
    plt.title("Population")
    plt.show()

    # gdp
    plt.plot(np.array([x["gdp"] for x in logs]))
    plt.title("GDP")
    plt.show()

    # human development index
    plt.plot(np.array([x["human_development"] for x in logs]))
    plt.title("Human Development Index")
    plt.show()

    # natural resources
    plt.plot(np.array([x["natural_resources"] for x in logs]))
    plt.title("Natural Resources")
    plt.show()

    # imports
    plt.plot(np.array([x["imports"] for x in logs]))
    plt.title("Imports")
    plt.show()

    # exports
    plt.plot(np.array([x["exports"] for x in logs]))
    plt.title("Exports")
    plt.show()


    