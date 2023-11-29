from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        res_list = []
        for row in self.jobs_list:
            if row["max_salary"] != '' and row["max_salary"] != 'invalid' and row["max_salary"] not in res_list:
                number = row["max_salary"]
                res_list.append(int(float(number)))
        return(max(res_list))

    def get_min_salary(self) -> int:
        res_list = []
        for row in self.jobs_list:
            if row["min_salary"] != '' and row["min_salary"] != 'invalid' and row["min_salary"] not in res_list:
                res_list.append(int(row["min_salary"]))
        return(min(res_list))

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
