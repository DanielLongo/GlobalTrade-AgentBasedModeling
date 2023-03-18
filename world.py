# from country import USA, CHINA, RUSSIA
from params import *
import matplotlib.pyplot as plt
import numpy as np

class World():
    def __init__(self, countries, trade_relations):
        self.countries = countries
        self.country_names_to_index = {country.name: i for i, country in enumerate(countries)}
        self.country_names = [country.name for country in countries]
        # trade relations is tuple of (country1, country2) for every posible trade relation, no self trade or reverse trade of existing pari
        self.trade_relations = trade_relations
        self.logs = []

    def step(self):
        for country in self.countries:
            country.step()
        
        # simulate trade between countries
        for relation in self.trade_relations:
            country_a_name = list(relation["country_names"])[0] 
            country_a = self.countries[self.country_names_to_index[country_a_name]]
            country_b_name = list(relation["country_names"])[1]
            country_b = self.countries[self.country_names_to_index[country_b_name]]
            min_human_developement = min([country_a.human_development["human_development_index"], country_b.human_development["human_development_index"]])
            gdp_per_captia_delta = country_a.get_gdp_per_capita() - country_b.get_gdp_per_capita()
            average_gdp = country_a.gdp["gdp"] + country_b.gdp["gdp"]

            # TODO: add natural resources to trade score
            trade_score = gdp_per_captia_delta * (min_human_developement ** .5) * average_gdp * 10

            # adjust trade score according to trade relations
            trade_relation = None
            for relation in self.trade_relations:
                if relation["country_names"] == set([country_a.name, country_b.name]):
                    trade_relation = relation["friendliness"]
                    break
                if relation["country_names"] == set([country_b.name, country_a.name]):
                    trade_relation = relation["friendliness"]
                    break

            if trade_relation:
                trade_score *= trade_relation
            else:
                print("No trade relation found for", country_a.name, country_b.name)

            excess_ratio = 1/3
            # now adjust country imports and exports based on trade score
            if trade_score < 0:
                # country a exports more and imports less
                country_a.export += trade_score * 1 / excess_ratio
                country_a.imports -= trade_score
                country_b.export -= trade_score 
                country_b.imports += trade_score * 1 / excess_ratio

                # increase gdp of country a
                country_a.gdp["gdp"] *= 1.005

            elif trade_score > 0:
                # country a exports less and imports more
                country_a.export -= trade_score
                country_a.imports += trade_score * 1 / excess_ratio
                country_b.export += trade_score * 1 / excess_ratio
                country_b.imports -= trade_score

                # increase gdp of country b
                country_b.gdp["gdp"] *= 1.005

        # log data
        self.logs.append({
            "countries": {country.name: country.get_json() for country in self.countries}
        })

    def plot_logs(self, variables_to_plot):

        for variable in variables_to_plot:
            for country in self.countries:
                plt.plot([entry["countries"][country.name][variable] for entry in self.logs], label=country.name)
            plt.title(variable)
            plt.legend()
            plt.show()
        
if __name__ == "__main__":
    # countries = [USA, CHINA, RUSSIA]
    countries = all_countries

    # trade_relations = [{"countries": set([countries[i].name, countries[j].name]), "friendliness": .5} for i in range(len(countries)) for j in range(len(countries)) if i != j and i < j]
    # trade_relations = trade_relations_less_contested
    trade_relations = trade_relations_more_contested
    world = World(countries, trade_relations=trade_relations)
    for i in range(20):
        world.step()
    print(world.logs)

    world.plot_logs(["population", "gdp", "human_development", "imports", "exports", "gdp_per_capita"])

    # graph the results for each variable. one color line for each country

    # plot population

    