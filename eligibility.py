def check_eligibility(events_data, student_gpa, student_region, student_skills, student_mode=None):

    # Normalize inputs
    student_region = student_region.lower()
    student_skills = [s.lower().strip() for s in student_skills]

    eligible = []

    for row in events_data:

        # GPA rule
        if student_gpa < row["min_gpa"]:
            continue

        # Region rule
        if not (row["region"] == "national" or row["region"] == student_region):
            continue

        # Skills rule
        event_skills = [s.strip().lower() for s in row["skills"].split(",")]
        if not any(skill in event_skills for skill in student_skills):
            continue

        # Mode rule (optional)
        if student_mode:
            if student_mode.lower() not in row["mode"]:
                continue

        # Add matching event
        eligible.append({
            "name": row["name"],
            "region": row["region"],
            "mode": row["mode"],
            "skills": row["skills"],
            "min_gpa": row["min_gpa"]
        })

    return eligible
