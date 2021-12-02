use std::env;
use std::vec::Vec;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let args: Vec<String> = env::args().collect();
    let mut h: i32 = 0;
    let mut d: i32 = 0;
    let mut d2: i32 = 0;
    let mut a: i32 = 0;

    if let Ok(lines) = read_lines(&args[1])
    {
        for line in lines
        {
            if let Ok(l) = line {
                let parts: Vec<&str> = l.split(' ').collect();
                let delta: i32 = parts[1].parse::<i32>().unwrap();
                if parts[0] == "forward" {
                    h += delta;
                    d2 += a * delta;
                }
                else if parts[0] == "down" {
                    d += delta;
                    a += delta;
                }
                else if parts[0] == "up" {
                    d -= delta;
                    a -= delta;
                }
            }
        }
        println!("Part 1: {}", h * d);
        println!("Part 2: {}", h * d2);
    }
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
