class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        result = []
        for row in image:
            flip = row[::-1]
            invert = []
            for value in flip:
                if value == 0 :
                    invert.append(1)
                else:
                    invert.append(0)
            result.append(invert)
        return result        