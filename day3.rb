def most(nums, index)
  ones = 0
  for i in 0..(nums.length - 1)
    if nums[i][index] == '1'
      ones += 1
    end
  end
  if (ones * 2) >= nums.length
    return 1
  end
  return 0
end

def least(nums, index)
  ones = 0
  for i in 0..(nums.length - 1)
    if nums[i][index] == '1'
      ones += 1
    end
  end
  if (ones * 2) < nums.length
    return 1
  end
  return 0
end

def filter(bit, nums)
  value = ''
  for i in 0..((nums[0].length) -1)
    count2 = 0
    nums2 = []
    if bit == 1
      cbit = most(nums, i)
    else
      cbit = least(nums, i)
    end
    value += '01'[cbit]
    for j in 0..(nums.length - 1)
      if nums[j][0..i] == value
        nums2[count2] = nums[j]
        count2 += 1
      end
    end
    nums = nums2
    if nums.length == 1
      return nums[0]
    end
  end
  return value
end

nums = []

File.open(ARGV[0]).each do |line|
  nums.append(line.strip)
end

gamma = 0
epsilon = 0
a = filter(1, nums)
b = filter(0, nums)
c = 0
d = 0
for i in 0..((nums[0]).length - 1)
  gamma *= 2
  epsilon *= 2
  c *= 2
  d *= 2
  gamma += most(nums, i)
  epsilon += least(nums, i)
  if a[i] == '1'
    c += 1
  end
  if b[i] == '1'
    d += 1
  end
end
puts "Part 1: #{gamma * epsilon}"
puts "Part 2: #{c * d}"

