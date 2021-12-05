input = File.read(ARGV[0]).split.map(&:to_s)
part1 = 0
part2 = 0
for i in 1..(input.length - 1)
  if input[i] > input[i - 1]
    part1 += 1
  end
end

for i in 0..(input.length - 4)
  if input[i] < input[i + 3]
    part2 += 1
  end
end

puts "Part 1 #{part1}"
puts "Part 2 #{part2}"
