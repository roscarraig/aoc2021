def generation(shoal)
  x = shoal.shift()
  shoal.push(0)
  shoal[6] += x
  shoal[8] += x
end

shoal = [0] * 10
total = 0

File.open(ARGV[0]).read.strip.split(',').each do |fish|
  shoal[fish.to_i] += 1
  total += 1
end
for gen in 1..80
  total += generation(shoal)
end
puts "Part 1: #{total}"
for gen in 81..256
  total += generation(shoal)
end
puts "Part 2: #{total}"
