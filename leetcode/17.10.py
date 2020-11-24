# 数组中占比超过一半的元素称之为主要元素。给定一个整数数组，找到它的主要元素。若没有，返回-1。
#
# 示例 1：
#
# 输入：[1,2,5,9,5,9,5,5,5]
# 输出：5
#  
#
# 示例 2：
#
# 输入：[3,2]
# 输出：-1
#  
#
# 示例 3：
#
# 输入：[2,2,1,1,1,2,2]
# 输出：2
#  
#
# 说明：
# 你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/find-majority-element-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
摩尔投票法
'''
class Solution:
    def majorityElement(self, List):
        major = 0
        cnt = 0
        for i in List:
            if(cnt == 0):
                major = i
                cnt = 1
            if(major == i):
                cnt = cnt +1
            elif(major != i):
                cnt = cnt -1
        t = 0
        for i in List:
            if(i == major):
                t = t + 1
        if(t >= len(List)+1):
            return major
        else:
            return -1
if __name__ == "__main__":
    list = [3,2,3]
    p = Solution()
    print(p.majorityElement(list))
