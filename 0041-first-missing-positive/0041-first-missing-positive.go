func firstMissingPositive(nums []int) int {
    n := len(nums)
    m := 0
    for i:=0; i < n; i++ {
        if nums[i] < 0 {
            nums[i] = 0
        } else if nums[i] > m {
            m = nums[i]
        }
    }

    m++;
    for _, num := range nums {
        orig := num
        if orig >= m {
            orig -= m
        }

        if orig > 0 && orig <= n && nums[orig - 1] < m {
            nums[orig - 1] += m
        }

    }

    for i:=0; i < n; i++ {
        if nums[i] < m {
            return i + 1
        }
    }

    return n + 1
}