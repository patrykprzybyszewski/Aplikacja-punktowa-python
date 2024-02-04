# points_app/models.py

class PointsApp:
    def __init__(self):
        self.user_points = {}
        self.pending_tasks = {}

    def add_points(self, user, activity, points):
        if user in self.user_points:
            if activity in self.user_points[user]:
                self.user_points[user][activity] += points
            else:
                self.user_points[user][activity] = points
        else:
            self.user_points[user] = {activity: points}

    def show_points(self, user):
        return self.user_points.get(user, {})

    def redeem_points_for_reward(self, user, reward, points_required):
        if user in self.user_points:
            user_points_total = self.user_points[user].get("Total", 0)
            if user_points_total >= points_required:
                self.user_points[user]["Total"] -= points_required
                return f"{user} redeemed {points_required} points for {reward}!"
            else:
                return f"{user} doesn't have enough points to redeem for {reward}."
        else:
            return f"{user} has no points."

    def mark_task_completed(self, user, task):
        if user in self.user_points:
            if user in self.pending_tasks and task in self.pending_tasks[user]:
                return f"{user}'s task '{task}' is already marked as completed."
            else:
                if user not in self.pending_tasks:
                    self.pending_tasks[user] = []
                self.pending_tasks[user].append(task)
                return f"{user} marked task '{task}' as completed. Awaiting approval."
        else:
            return f"{user} has no points."

    def approve_task_and_award_points(self, user, task, points):
        if user in self.user_points and task in self.pending_tasks.get(user, []):
            self.add_points(user, task, points)
            self.pending_tasks[user].remove(task)
            return f"{user} approved and awarded {points} points for completing task '{task}'."
        else:
            return f"{user} cannot approve or award points for task '{task}'."

# Sample usage of the application
app = PointsApp()

app.add_points("Son-in-law", "Cleaning", 5)
app.add_points("Son-in-law", "Laundry", 8)
app.add_points("Son-in-law", "Mowing the lawn", 15)

app.add_points("Mother-in-law", "Floor cleaning", 3)
app.add_points("Mother-in-law", "Grocery shopping", 7)
app.add_points("Mother-in-law", "Gardening help", 5)
app.add_points("Mother-in-law", "Feeding animals", 10)

app.mark_task_completed("Mother-in-law", "Mowing the lawn")
print("Pending tasks for Mother-in-law:", app.pending_tasks.get("Mother-in-law", []))

print(app.approve_task_and_award_points("Mother-in-law", "Mowing the lawn", 20))
print("Mother-in-law's points:", app.show_points("Mother-in-law"))
