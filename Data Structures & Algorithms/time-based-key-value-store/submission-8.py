class TimeMap:

    def __init__(self):
        self.container = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.container:
            self.container.update({key: [(value, timestamp)]})   
        else:
            self.container[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.container:
            return ""
            
        box = self.container[key]

        left = 0
        right = len(box) - 1
        result = ""

        while left <= right:
            mid = left + (right - left) // 2
            if box[mid][1] <= timestamp:
                result = box[mid][0]
                left = mid + 1
            else:
                right = mid - 1
                
        return result
