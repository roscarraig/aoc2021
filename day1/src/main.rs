use std::env;
use std::vec::Vec;
use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut numbers: Vec<i32> = Vec::new();
    let args: Vec<String> = env::args().collect();

    if let Ok(lines) = read_lines(&args[1])
    {
        for line in lines
        {
            if let Ok(num) = line
            {
                numbers.push(num.parse().unwrap());
            }
        }
    }
    println!("Part 1: {}", count_step1(&numbers));
    println!("Part 2: {}", count_step2(&numbers));
}

fn count_step1(v: &Vec<i32>) -> i32
{
    let mut result: i32 = 0;
    let l = v.len();

    for i in  0..(l - 1)
    {
        if v[i] < v[i + 1]
        {
            result += 1;
        }
    }
    return result;
}

fn count_step2(v: &Vec<i32>) -> i32
{
    let mut result: i32 = 0;
    let l = v.len();

    for i in  0..(l - 3)
    {
        if v[i] < v[i + 3]
        {
            result += 1;
        }
    }
    return result;
}

// The output is wrapped in a Result to allow matching on errors
// Returns an Iterator to the Reader of the lines of the file.
fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where P: AsRef<Path>, {
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}
