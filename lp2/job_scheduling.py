def job_scheduling(jobs):
    # Sort the jobs based on their deadlines in ascending order
    sorted_jobs = sorted(jobs, key=lambda x: x[1])

    schedule = []
    current_time = 1

    for job in sorted_jobs:
        job_id, deadline, duration = job

        # Check if the job can be scheduled without missing its deadline
        if current_time + duration <= deadline:
            schedule.append(job)
            current_time += duration

    return schedule

# Example usage:
jobs = [(1, 5, 2),  # (job_id, deadline, duration)
        (2, 3, 1),
        (3, 7, 4),
        (4, 2, 1),
        (5, 6, 3)]

result = job_scheduling(jobs)
print("Scheduled jobs:")
for job in result:
    print(f"Job {job[0]} - Deadline: {job[1]}, Duration: {job[2]}")