from app.sections import Section
from datetime import datetime
from utils.colors import colors
import csv


class Timetable:
    def __init__(self):
        self.timetable = {}
        self.exam_timetable = {}

    def enroll_subject(self, course: object, section: str):
        course_section = Section(course)
        timeslot = course_section.get_datetime(section)
        timeslot[2] = datetime.strptime(timeslot[2], "%H:%M")
        timeslot[3] = datetime.strftime(timeslot[3], "%H:%M")
        days_of_week = timeslot[0].split(",")
        clash = self.check_clashes(days_of_week, timeslot)
        if not clash:
            for day in days_of_week:
                if day not in self.timetable:
                    self.timetable[day] = []
                    self.timetable[day].append(timeslot[1:3])
                else:
                    self.timetable[day].append(timeslot[1:3])

    def check_clashes(self, days_of_week: list, timeslot: list):
        for day in days_of_week:
            if day not in self.timetable:
                pass
            else:
                for subject in self.timetable[day]:
                    if subject[1] > timeslot[2] and subject[2] > timeslot[3]:
                        pass
                    elif subject[1] < timeslot[2] and subject[2] < timeslot[3]:
                        pass
                    else:
                        print(
                            colors.FAIL
                            + f"Clash detected with {subject[0]} on {day}"
                            + colors.ENDC
                        )
                        return True
        return False

    def export_to_csv(self):
        with open(f"Timetable_{datetime.now()}.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Day", "Subject", "Start Time", "End Time"])
            for day in self.timetable:
                for subject in self.timetable[day]:
                    writer.writerow([day] + subject)