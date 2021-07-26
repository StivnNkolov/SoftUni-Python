from Gym04.customer import Customer
from Gym04.equipment import Equipment
from Gym04.exercise_plan import ExercisePlan
from Gym04.gym import Gym
from Gym04.subscription import Subscription
from Gym04.trainer import Trainer


if __name__ == '__main__':
    customer = Customer("John", "Maple Street", "john.smith@gmail.com")
    equipment = Equipment("Treadmill")
    trainer = Trainer("Peter")
    subscription = Subscription("14.05.2020", 1, 1, 1)
    plan = ExercisePlan(1, 1, 20)

    gym = Gym()

    gym.add_customer(customer)
    gym.add_equipment(equipment)
    gym.add_trainer(trainer)
    gym.add_plan(plan)
    gym.add_subscription(subscription)

    print(Customer.get_next_id())

    print(gym.subscription_info(1))
