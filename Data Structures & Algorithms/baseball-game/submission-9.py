class Solution:
    def calPoints(self, operations: List[str]) -> int:
        records = []
        for o in operations:
            try:
                records.append(int(o))
            except ValueError:
                if o == "+":
                    records.append(records[-2] + records[-1])
                elif o == "D":
                    records.append(records[-1]*2)
                elif o == "C":
                    records.pop()
        return sum(records)