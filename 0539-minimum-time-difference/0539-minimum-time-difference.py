class Solution:
    def findMinDifference(self, timePoints):
        minutes = []

        for time in timePoints:
            hour = int(time[:2])
            minute = int(time[3:])
            minutes.append(hour * 60 + minute)

        minutes.sort()

        ans = 1440  # minutes in one day

        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])

        # Difference across midnight
        ans = min(ans, 1440 - minutes[-1] + minutes[0])

        return ans