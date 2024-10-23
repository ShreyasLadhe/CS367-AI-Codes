import random
import matplotlib.pyplot as plt

random.seed(10)

class BinaryBandit:
    def __init__(self):  
        self.num_arms = 2  

    def avail_act(self):
        return list(range(self.num_arms))

    def binBandA(self, action):
        probabilities = [0.1, 0.2] 
        value = random.random()
        return 1 if value < probabilities[action] else 0

    def binBandB(self, action):
        probabilities = [0.8, 0.9]  
        value = random.random()
        return 1 if value < probabilities[action] else 0

def ep_greedy(bandit, epsilon, iterations, use_banditA=True):
    q_val = [0] * bandit.num_arms  
    act_count = [0] * bandit.num_arms  
    tot_rewards = []
    avg_rewards = [0]

    for iteration in range(iterations):
        if random.random() > epsilon:
            chosen_action = q_val.index(max(q_val)) 
        else:
            chosen_action = random.choice(bandit.avail_act())  

        if use_banditA:
            reward = bandit.binBandA(chosen_action)
        else:
            reward = bandit.binBandB(chosen_action)
        
        tot_rewards.append(reward)
        act_count[chosen_action] += 1
        q_val[chosen_action] += (reward - q_val[chosen_action]) / act_count[chosen_action]
        avg_rewards.append(avg_rewards[-1] + (reward - avg_rewards[-1]) / (iteration + 1))

    return q_val, avg_rewards, tot_rewards


random.seed(10)
bandit = BinaryBandit()

Q_A, avg_rewards_A, rewards_A = ep_greedy(bandit, 0.2, 2000, use_banditA=True)
Q_B, avg_rewards_B, rewards_B = ep_greedy(bandit, 0.2, 2000, use_banditA=False)

fig, (axis1, axis2) = plt.subplots(1, 2, figsize=(15, 5))

axis1.plot(avg_rewards_A, label="Bandit A")
axis1.plot(avg_rewards_B, label="Bandit B")
axis1.title.set_text("Average Rewards vs Iterations")
axis1.set_xlabel("Iterations")
axis1.set_ylabel("Average Reward")
axis1.legend()

axis2.plot(rewards_A, label="Bandit A")
axis2.plot(rewards_B, label="Bandit B")
axis2.title.set_text("Rewards per Iteration")
axis2.set_xlabel("Iterations")
axis2.set_ylabel("Reward")
axis2.legend()

plt.show()