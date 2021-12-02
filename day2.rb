h = 0
d = 0
d2 = 0
a = 0

File.open(ARGV[0]).each do |line|
  move, dist = line.split(' ')
  dist = dist.to_i
  if move == 'forward'
    h += dist
    d2 += a * dist
  elsif move == 'down'
    d += dist
    a += dist
  elsif move == 'up'
    d -= dist
    a -= dist
  end
end

puts("Part 1: #{h * d}")
puts("Part 2: #{h * d2}")
