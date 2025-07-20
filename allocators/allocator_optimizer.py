import random

import numpy as np


class StrategyGenome:
    def __init__(self, weights):
        self.weights = np.array(weights)
        self.fitness = 0

    def mutate(self, rate=0.1):
        for i in range(len(self.weights)):
            if random.random() < rate:
                self.weights[i] += np.random.normal(0, 0.1)
        self.weights = np.clip(self.weights, 0, 1)
        self.weights /= np.sum(self.weights)  # Normalize


class CapitalOptimizer:
    def __init__(self, strategy_count):
        self.population = [
            StrategyGenome(np.random.dirichlet(np.ones(strategy_count))) for _ in range(20)
        ]

    def evaluate(self, strategy_returns):
        for genome in self.population:
            weighted_return = np.dot(genome.weights, strategy_returns)
            genome.fitness = weighted_return

    def evolve(self):
        self.population.sort(key=lambda g: g.fitness, reverse=True)
        survivors = self.population[:5]
        new_population = survivors[:]
        while len(new_population) < len(self.population):
            parent = random.choice(survivors)
            child = StrategyGenome(np.copy(parent.weights))
            child.mutate()
            new_population.append(child)
        self.population = new_population

    def best_weights(self):
        return self.population[0].weights
