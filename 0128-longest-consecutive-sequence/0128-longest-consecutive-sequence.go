func longestConsecutive(nums []int) int {
    if len(nums) < 1 {
        return 0
    }

    numsMap := map[int]bool{}
    for _, num := range nums {
        numsMap[num] = true
    }

    maxLen := 0
    currLen := 0
    for num := range numsMap {
        if _, ok := numsMap[num - 1]; !ok {
            currNum := num
            currLen = 1
            for numsMap[currNum + 1] {
                currNum += 1
                currLen += 1
            }

            if maxLen < currLen {
                maxLen = currLen
            }
        }
    }

    if maxLen < currLen {
        maxLen = currLen
    }

    return maxLen;
}