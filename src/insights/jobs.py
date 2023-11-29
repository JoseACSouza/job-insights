from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            file_reader = csv.reader(file, delimiter=",", quotechar='"')
            header, *data = file_reader
            response = []
            for row in data:
                obj = {}
                for index in range(len(row)):
                    obj[header[index]] = row[index]
                response.append(obj)
        self.jobs_list = response

    def get_unique_job_types(self) -> List[str]:
        pass

    def filter_by_multiple_criteria(self) -> List[dict]:
        pass
