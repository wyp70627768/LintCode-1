class Solution:
    """
    @param area: web pageâs area
    @return: the length L and the width W of the web page you designed in sequence
    """

    def constructRectangle(self, area):
        # Write your code here
        # results=[]
        # W=1
        # L=area//W
        # results.append((L,W,L-W))
        # while L>=W :
        #     W+=1
        #     if area%W==0:
        #         L=area//W
        #         if L>=W:
        #             results.append([L,W,L-W])
        # print(results)
        # results=sorted(results, key=lambda x: x[2])
        # print(results)
        # return results[0][0], results[0][1]

        temp = 1
        W = 1
        L = area // W
        while L >= W:
            if area % W == 0:
                L = area // W
                if L >= W:
                    templ = L
                    tempw = W
            W += 1
        return templ, tempw


test = Solution()
test.constructRectangle(50)
