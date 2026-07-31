class Solution:
    def calPoints(self, operations: list[str]) -> int:
        def is_integer(s):
            try:
                int(s)
                return True
            except ValueError:
                return False
        record = []
        for op in operations:
            if is_integer(op):
                record.append(int(op))
            elif op == "+":
                record.append(record[-2] + record[-1])
            elif op == "D":
                record.append(2*record[-1])
            elif op == "C":
                record.pop()
        return sum(record)


        