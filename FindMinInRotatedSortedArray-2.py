class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        print num;
        if len(num) == 1:
            return num[0];
        elif len(num) == 2:
            if num[0] >= num[1]:
                return num[1];
            else:
                return num[0];
        first = 0;
        mid = len(num)/2;
        last = len(num) - 1;
        if num[first] > num[mid] and num[mid] > num[last]:
            return num[last];
        elif num[first] > num[mid] and num[mid] < num[last]:
            return self.findMin(num[:mid+1]);
        elif num[first] < num[mid] and num[mid] < num[last]:
            return num[first];
        elif num[first] < num[mid] and num[mid] > num[last]:
            return self.findMin(num[mid:]);
        elif num[first] == num[mid] and num[mid] != num[last]:
            return self.findMin(num[mid:]);
        elif num[mid] == num[last] and num[first] != num[first]:
            return self.findMin(num[:mid+1]);
        else:
            return self.findMin(num[1:len(num)-1])

a = [3,3,3,1,3]
m = Solution()
print m.findMin(a)

