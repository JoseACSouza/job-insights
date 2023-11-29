from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        res_list = []
        for row in self.jobs_list:
            holder = row["max_salary"]
            if holder != '' and holder != 'invalid' and holder:
                res_list.append(int(holder))
        return(max(res_list))

    def get_min_salary(self) -> int:
        res_list = []
        for row in self.jobs_list:
            holder = row["min_salary"]
            if holder != '' and holder != 'invalid' and holder:
                res_list.append(int(holder))
        return(min(res_list))

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
