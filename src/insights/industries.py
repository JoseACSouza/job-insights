from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        res_list = []
        for row in self.jobs_list:
            if row["industry"] != '' and row["industry"] not in res_list:
                res_list.append(row["industry"])
        return(res_list)
