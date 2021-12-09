floor = []

def mark_basin(i, j, floor)
  size = 0

  if floor[i][j] == '9'
    return 0
  end

  floor[i][j] = '9'
  size += 1

  if i > 0
    size += mark_basin(i - 1, j, floor)
  end
  if j > 0
    size += mark_basin(i, j - 1, floor)
  end
  if i < floor.length - 1
    size += mark_basin(i + 1, j, floor)
  end
  if j < floor[0].length - 1
    size += mark_basin(i, j + 1, floor)
  end
  return size
end

File.open(ARGV[0]).each do |line|
  floor.append(line.strip)
end

rl = floor[0].length - 1
ml = floor.length - 1
basins = []
part1 = 0
part2 = 1

for i in 0..ml
  for j in 0..rl
    x = floor[i][j]
    if !((i > 0 and x >= floor[i - 1][j]) or (j > 0 and x >= floor[i][j - 1]) or (j < rl and x  >= floor[i][j + 1]) or (i < ml and x >= floor[i + 1][j]))
      part1 += x.to_i + 1
    end
  end
end

puts "Part 1: #{part1}"

for i in 0..ml
  for j in 0..rl
    s = mark_basin(i, j, floor)
    if s > 0
      basins.append(s)
    end
  end
end

for x in basins.sort.last(3)
  part2 *= x
end
puts "Part 2: #{part2}"
